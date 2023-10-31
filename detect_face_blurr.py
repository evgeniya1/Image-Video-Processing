#%%
import cv2
import numpy as np

video = cv2.VideoCapture('smile.mp4')
success, frame = video.read()
height = frame.shape[0]
width = frame.shape[1]
n_colors = frame.shape[2]
face_cascade = cv2.CascadeClassifier('faces.xml')

output = cv2.VideoWriter('blurred_smile.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 1
while success:
    print('frame #', count)
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    for (x, y, w, h) in faces:
        ##blured rectangle
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        ##white rectangle
        #frame[y:y+h, x:x+w] = np.ones((h,w,n_colors), np.uint8)*255
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), -1)

    output.write(frame)
    count += 1
    success, frame = video.read()

output.release()
video.release()
# %%
