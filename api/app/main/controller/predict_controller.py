# app/controller/predict_controller.py
import base64
from flask_restx import Namespace, Resource
from flask import request, jsonify
import numpy as np
from torchvision import transforms
from app.auth_middleware import jwt_required
from app.main.model.yolov8_model import load_model
from ..util.dto import predict_dto
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.DEBUG)

api = predict_dto.api
model = load_model()

@api.expect(predict_dto.parser)
@api.doc(responses={
    200: 'Success',
    400: 'No images uploaded',
    500: 'Internal Server error'
})
@api.route('/')
class Predict(Resource):

    @jwt_required()
    def post(self):
        if 'images' not in request.files:
            return {'error': 'No images uploaded'}, 400

        files = request.files.getlist('images')

        if len(files) == 0:
            return {'error': 'At least one image should be uploaded for prediction'}, 400

        try:
            results = self.process_images(files)
            return jsonify(results)
        except Exception as e:
            logging.error(f'Error processing images: {e}')
            return {'error': 'Internal Server Error'}, 500

    def process_images(self, files):
        deformed_cells_total = 0
        healthy_cells_total = 0
        annotated_images = []

        transform = transforms.Compose([
            transforms.Resize((640, 640)),
            transforms.Lambda(lambda img: img.rotate(-90)),
            transforms.ToTensor(),  # Converts the image to a Tensor
        ])

        for file in files:
            try:
                image = Image.open(io.BytesIO(file.read()))
                image = transform(image).unsqueeze(0)  # Add batch dimension
                image = image.float()

                results = model(image, conf=0.6, max_det=600)

                for result in results:
                    boxes = result.boxes  # Boxes object for bounding box outputs
                    unique, counts = np.unique(boxes.cls.cpu().numpy(), return_counts=True)
                    annotated_image = result.plot(labels=False)  # Get the annotated image as NumPy array

                    img = Image.fromarray(annotated_image.astype('uint8'))
                    buff = io.BytesIO()
                    img.save(buff, format="JPEG")
                    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
                    annotated_images.append(new_image_string)

                    if len(counts) > 0:
                        deformed_cells_total += int(counts[0])
                    if len(counts) > 1:
                        healthy_cells_total += int(counts[1])
            except Exception as e:
                logging.error(f'Error processing file {file.filename}: {e}')
                continue

        total_cells_detected = deformed_cells_total + healthy_cells_total

        return {
            'deformedCellsDetected': deformed_cells_total,
            'healthyCellsDetected': healthy_cells_total,
            'totalCellsDetected': total_cells_detected,
            'annotatedImages': annotated_images
        }
