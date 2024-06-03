# app/controller/predict_controller.py
from flask_restx import Namespace, Resource
from flask import request, jsonify, send_file
import torch
from torchvision import transforms
from app.main.model.yolov8_model import load_model
from PIL import Image
import io

predict_ns = Namespace('predict', description='Prediction operations')

model = load_model()

def recursive_tensor_to_list(value):
    """ Recursively convert tensors in nested lists and tuples to lists. """
    if isinstance(value, torch.Tensor):
        return value.tolist()  # Convert tensors to list
    elif isinstance(value, (list, tuple)):
        return [recursive_tensor_to_list(item) for item in value]  # Recurse into lists/tuples
    return value  # Return non-tensor items unchanged

@predict_ns.route('/')
class Predict(Resource):
    def post(self):
        print(">>>> PREDICT")
        if 'image' not in request.files:
            return {'error': 'No image uploaded'}, 400

        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))

        transform = transforms.Compose([
        transforms.Resize((640, 640)),  # Adjust size according to your model's requirements
        transforms.ToTensor(),  # Converts the image to a Tensor
        # Add normalization if your model was trained with it:
        # transforms.Normalize(mean=[mean values], std=[std values]),
        ])
    
        # Apply the transformations
        image = transform(image).unsqueeze(0)  # Add batch dimension
        
        image = image.float()

        # Perform inference
        with torch.no_grad():
            outputs = model(image)
    
        
        # Format the results as needed
        # predictions = outputs.tolist()
        print(">>>> Results")
         # Check output type and structure
        # print(outputs)
        for tensor in outputs:
            if isinstance(tensor, torch.Tensor):
                print("Tensor shape:", tensor.shape)
            elif isinstance(tensor, list):
            # If the element is a list of tensors, print each tensor's shape
                for t in tensor:
                    print("Tensor in list shape:", t.shape)
            else:
                print("Element is neither tensor nor list")
    
        predictions = recursive_tensor_to_list(outputs)

        return jsonify({'predictions': predictions})

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
