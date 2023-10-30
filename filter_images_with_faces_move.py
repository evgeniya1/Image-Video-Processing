import cv2
import os
from pathlib import Path

check_dir = Path('./check_faces')
save_dir = Path('./filter_with_faces')
face_cascade = cv2.CascadeClassifier('faces.xml')

images_with_faces = []

for file in check_dir.iterdir():
    image = cv2.imread(str(file))
    faces = face_cascade.detectMultiScale(image, 1.11, 4)

    if len(faces) > 0:
        images_with_faces.append(file)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

        save_filepath = str(save_dir) + '/' +  file.stem + file.suffix
        cv2.imwrite(save_filepath, image)
# %%
