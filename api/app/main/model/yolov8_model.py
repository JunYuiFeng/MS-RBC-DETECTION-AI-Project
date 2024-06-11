import os
from ultralytics import YOLO

def load_model() :
    model_path = os.path.join(os.path.dirname(__file__), 'yolov8m_v3.0.pt')
    model = YOLO(model_path)
    return model 