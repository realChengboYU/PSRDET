
import cv2

# 引入YOLO模型
from ultralytics import YOLO
model= YOLO("runs/exp25/weights/best.pt")
model(source='/home/dell/桌面/sdd/redetr_m3fd/detr_m3fd/images/test',save=True,name='detect')
