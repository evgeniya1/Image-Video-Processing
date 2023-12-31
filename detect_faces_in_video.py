#%%
import cv2
from datetime import datetime
face_cascade = cv2.CascadeClassifier('faces.xml')

video = cv2.VideoCapture('video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
print(width, height, nr_frames, fps)

#extract all frames
success, frame = video.read()

output = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while success:

    faces = face_cascade.detectMultiScale(frame, 1.2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)

    output.write(frame)

    success, frame = video.read()


output.release()
