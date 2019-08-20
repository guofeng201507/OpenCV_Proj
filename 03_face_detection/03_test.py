import cv2

filepath = "ironman.png"
img = cv2.imread(filepath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

classifier = cv2.CascadeClassifier(
    r'C:\Users\guofe\workspace\OpenCV_Proj\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
    )

color = (0, 255, 0)

faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):
    for faceRect in faceRects:
        x, y, w, h = faceRect
        # face
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # left eye
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        # right eye
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        # mouth
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow("image", img)
c = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
