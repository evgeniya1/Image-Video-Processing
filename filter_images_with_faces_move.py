import cv2
import os
from pathlib import Path

INPUT_FOLDER = Path('./check_faces')
OUTPUT_FOLDER = Path('./filter_with_faces')
CASCADE = cv2.CascadeClassifier('faces.xml')
COLOR = (255, 255, 255)
NEIGHBORS = 4
SCALE = 1.2

images_with_faces = []

for file in INPUT_FOLDER.iterdir():
    image = cv2.imread(str(file))
    faces = CASCADE.detectMultiScale(image, SCALE, NEIGHBORS)

    if len(faces) > 0:
        images_with_faces.append(file)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), COLOR, NEIGHBORS)

        save_filepath = str(OUTPUT_FOLDER) + '/' +  file.stem + file.suffix
        cv2.imwrite(save_filepath, image)
