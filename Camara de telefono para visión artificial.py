# Camara de telefono para visión artificial
import cv2
import numpy as np
url = 'Tu dirección de IP/video'
cp = cv2.VideoCapture(url)
while (True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow('Frame', frame)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
    cv2.destroyAllWindows()