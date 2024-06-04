# app/controller/predict_controller.py
import base64
import cv2
from flask_restx import Namespace, Resource
from flask import request, jsonify, send_file
import numpy as np
import torch
from torchvision import transforms
from app.main.model.yolov8_model import load_model
from PIL import Image
import io

predict_ns = Namespace('predict', description='Prediction operations')

model = load_model()

@predict_ns.route('/')
class Predict(Resource):
    def post(self):
        if 'image' not in request.files:
            return {'error': 'No image uploaded'}, 400

        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))

        transform = transforms.Compose([
        transforms.Resize((640, 640)),  
        transforms.ToTensor(),  # Converts the image to a Tensor
        ])
    
        # Apply the transformations
        image = transform(image).unsqueeze(0)  # Add batch dimension
        image = image.float()

        results = model(image, conf=0.6)

        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            unique, counts = np.unique(boxes.cls.numpy(), return_counts=True)
            annotated_image = result.plot()  # Get the annotated image as NumPy array

            # Convert image to bytes (assuming RGB format)
            encoded_image = base64.b64encode(annotated_image.tobytes()).decode('utf-8')
       
        return jsonify({
            'deformedCellsDetected': int(counts[0]),
            'healthyCellsDetected': int(counts[1]),
            'annotatedImage': encoded_image
                        })

