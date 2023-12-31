#%%
import cv2
from datetime import datetime
face_cascade = cv2.CascadeClassifier('faces.xml')

video = cv2.VideoCapture(0) #0 - integrated camera

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
print(width, height, nr_frames, fps)

#extract all frames
success, frame = video.read()

output = cv2.VideoWriter("mac_video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height))

count = 1
while success&(count<=1000):
    print(count)
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)

    cv2.imshow("Recording", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    output.write(frame)
    success, frame = video.read()
    count += 1

output.release()
video.release()
cv2.destroyAllWindows()
# %%
