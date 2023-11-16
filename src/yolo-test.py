from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("2023-11-14 13.33.10.png",show=True)

cv2.waitKey(0)