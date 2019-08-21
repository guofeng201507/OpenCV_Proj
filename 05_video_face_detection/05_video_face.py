# -*- coding:utf-8 -*-

import cv2


def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier(
        r'C:\Users\guofe\workspace\OpenCV_Proj\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
    )
    faceRects = cap.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # face
    cv2.imshow("Image", img)


cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    detect_face(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
