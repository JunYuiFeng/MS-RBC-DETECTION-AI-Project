import torch
import os
# from model import CustomYOLOv8

def load_model(model_path=None):
    if model_path is None:
        model_path = os.path.join(os.path.dirname(__file__), 'yolov8m_v2.0.pt')
    model = torch.load(model_path)
    # model = CustomYOLOv8()
    # model.load_state_dict(torch.load(model_path))
    # model.eval()
    return model