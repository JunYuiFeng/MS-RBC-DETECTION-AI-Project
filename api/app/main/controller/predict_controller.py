# app/controller/predict_controller.py
from flask_restx import Namespace, Resource
from flask import request, jsonify, send_file
from app.main.model.yolov8_model import load_model
from PIL import Image
import io

predict_ns = Namespace('predict', description='Prediction operations')

model = load_model()

@predict_ns.route('/')
class Predict(Resource):
    def post(self):
        print(">>>> PREDICT")
        print(model)
        if 'image' not in request.files:
            return {'error': 'No image uploaded'}, 400

        file = request.files['image']
        img = Image.open(file.stream)
        
        # Perform inference
        results = model(img)

        # Annotate image
        annotated_img = results.render()[0]
        annotated_img_pil = Image.fromarray(annotated_img)

        # Convert image to byte array
        img_io = io.BytesIO()
        annotated_img_pil.save(img_io, 'JPEG')
        img_io.seek(0)

        # Extract other results if needed
        detections = results.pandas().xyxy[0].to_dict(orient="records")

        return jsonify({
            'annotations': detections,
            'image': request.url_root + 'predict/annotated_image'
        })

@predict_ns.route('/annotated_image')
class AnnotatedImage(Resource):
    def get(self):
        return send_file(img_io, mimetype='image/jpeg')
