import os
os.environ["CUDA_VISIBLE_DEVICES"]='1'
from ultralytics import YOLO


if __name__ == "__main__":
    # Load a model
    pth_path = r"runs/exp15/weights/best.pt"
    # model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model

    # Validate the model
    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category