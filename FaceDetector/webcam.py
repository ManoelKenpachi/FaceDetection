import cv2
from cvzone.FaceDetectionModule import FaceDetector

VIDEO = cv2.VideoCapture(0) # 0 para webcam padrão
DETECTOR = FaceDetector()

while True:
    _, img = VIDEO.read()
    img, boxes = DETECTOR.findFaces(img, draw=True)
    cv2.imshow('Resultado', img)
    if cv2.waitKey(1) ==27:
        break
