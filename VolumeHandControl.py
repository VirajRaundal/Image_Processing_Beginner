import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm

########################
wCam, hCam = 640, 480
########################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4,hCam)
pTime = 0
detector = htm.handDetector()



while True:
    success, img = cap.read()
    img = detector.findHands(img)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (50,70), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)