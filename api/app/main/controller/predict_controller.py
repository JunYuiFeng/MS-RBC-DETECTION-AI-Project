# app/controller/predict_controller.py
import base64
import cv2
from flask_restx import Namespace, Resource
from flask import request, jsonify, send_file
import numpy as np
import torch
from torchvision import transforms
from app.auth_middleware import jwt_required
from app.main.model.yolov8_model import load_model
from ..util.dto import predict_dto
from PIL import Image
import io
import logging
logging.basicConfig(level=logging.DEBUG)
import random

print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())


api = predict_dto.api
model = load_model()



seed = 42
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
if torch.cuda.is_available():
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# @api.marshal_with(predict_dto.predict_data)
@api.expect(predict_dto.parser)
@api.doc(responses={
    200: 'Success',
    400: 'No image uploaded',
    500: 'Internal Server error'
})
@api.route('/')
class Predict(Resource):

    @jwt_required()
    def post(self):
        if 'image' not in request.files:
            return {'error': 'No image uploaded'}, 400
        logging.error(f'format: {request}')
        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))


        transform = transforms.Compose([
            transforms.Resize((640, 640)),
            transforms.CenterCrop(640),
            transforms.ToTensor(),  # Converts the image to a Tensor
        ])

        # Apply the transformations
        image = transform(image).unsqueeze(0)  # Add batch dimension
        image = image.float()

        results = model(image, conf=0.6)

        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs

            # Move the tensor to the CPU and convert to numpy
            unique, counts = np.unique(boxes.cls.cpu().numpy(), return_counts=True)
            annotated_image = result.plot(labels=False)  # Get the annotated image as NumPy array

            img = Image.fromarray(annotated_image.astype('uint8'))
            buff = io.BytesIO()
            img.save(buff, format="JPEG")
            new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

            deformed_cells = 0
            healthy_cells = 0
            if len(counts) > 0:
                deformed_cells = int(counts[0])
            if len(counts) > 1:
                healthy_cells = int(counts[1])

            response = jsonify({
                'deformedCellsDetected': deformed_cells,
                'healthyCellsDetected': healthy_cells,
                'annotatedImage': new_image_string
            })
            return response
