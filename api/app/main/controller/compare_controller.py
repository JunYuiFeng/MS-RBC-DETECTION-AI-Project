# app/controller/compare_controller.py
import base64
from flask_restx import Namespace, Resource
from flask import request, jsonify
import numpy as np
from torchvision import transforms
from app.auth_middleware import jwt_required
from app.main.model.yolov8_model import load_model
from ..util.dto import comparepredict_dto
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.DEBUG)

compare_api = comparepredict_dto.api
model = load_model()

@compare_api.route('/')
class Compare(Resource):

    @compare_api.expect(comparepredict_dto.parser)
    @compare_api.doc(responses={
        200: 'Success',
        400: 'No images uploaded',
        500: 'Internal Server error'
    })
    @jwt_required()
    def post(self):
        #check for request files
        if 'patient1_images' not in request.files or 'patient2_images' not in request.files:
            return {'error': 'No images uploaded'}, 400

        patient1_files = request.files.getlist('patient1_images')
        patient2_files = request.files.getlist('patient2_images')

        if len(patient1_files) == 0 or len(patient2_files) == 0:
            return {'error': 'At least one image for each patient should be uploaded for comparison'}, 400
        
        # assign processed images to patients
        results_patient_1 = self.process_images(patient1_files)
        results_patient_2 = self.process_images(patient2_files)

        comparison_results = {
            'patient1': results_patient_1,
            'patient2': results_patient_2,
            'comparison': self.compare_results(results_patient_1, results_patient_2)
        }

        return jsonify(comparison_results)

    def process_images(self, files):
        deformed_cells_total = 0
        healthy_cells_total = 0
        annotated_images = []

        
        #apply general pre-processing to images for model input
        transform = transforms.Compose([
            transforms.Resize((640, 640)),
            transforms.Lambda(lambda img: img.rotate(-90)),
            transforms.ToTensor(),
        ])

        for file in files:
            image = Image.open(io.BytesIO(file.read()))
            image = transform(image).unsqueeze(0)  # Add batch dimension
            image = image.float()

            results = model(image, conf=0.6, max_det=600)

            # create imgs including boundingboxes
            for result in results:
                boxes = result.boxes  # Boxes object for bounding box outputs
                unique, counts = np.unique(boxes.cls.cpu().numpy(), return_counts=True)
                annotated_image = result.plot(labels=False)  # Get the annotated image as NumPy array

                # transform from array to img
                img = Image.fromarray(annotated_image.astype('uint8'))
                buff = io.BytesIO()
                img.save(buff, format="JPEG")
                new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
                annotated_images.append(new_image_string)

                if len(counts) > 0:
                    deformed_cells_total += int(counts[0])
                if len(counts) > 1:
                    healthy_cells_total += int(counts[1])

        total_cells_detected = deformed_cells_total + healthy_cells_total

        return {
            'deformedCellsDetected': deformed_cells_total,
            'healthyCellsDetected': healthy_cells_total,
            'totalCellsDetected': total_cells_detected,
            'annotatedImages': annotated_images
        }

    def compare_results(self, results1, results2):
        comparison = {
            'deformedCellsDifference': results1['deformedCellsDetected'] - results2['deformedCellsDetected'],
            'healthyCellsDifference': results1['healthyCellsDetected'] - results2['healthyCellsDetected'],
            'totalCellsDifference': results1['totalCellsDetected'] - results2['totalCellsDetected']
        }
        return comparison
