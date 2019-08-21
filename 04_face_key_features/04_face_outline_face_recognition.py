# coding=utf-8

import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("meinv.png")
empty_image = face_recognition.load_image_file("empty.png")

face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    facial_features = [
        'chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge', 'nose_tip',
        'left_eye', 'right_eye', 'top_lip', 'bottom_lip'
    ]
    pil_image = Image.fromarray(empty_image)
    pil_image = Image.fromarray(image)

    d = ImageDraw.Draw(pil_image)
    for facial_feature in facial_features:
        d.line(face_landmarks[facial_feature], fill=(255, 255, 255), width=2)
    pil_image.show()
