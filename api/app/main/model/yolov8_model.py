import torch
import os
# from model import CustomYOLOv8

def load_model() :
    model_path = os.path.join(os.path.dirname(__file__), 'yolov8m_v2.0.pt')
    model_dict = torch.load(model_path, map_location=torch.device('cpu'))
    model = model_dict['model']  # Extract the model
    model = model.float()  # Ensure the model is in full precision
    model.eval()  # Set the model to evaluation mode
    return model