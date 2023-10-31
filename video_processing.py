import cv2
from datetime import datetime

video = cv2.VideoCapture('video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

print(width, height, nr_frames, fps)

# #extract all frames
# success, frame = video.read()
# count = 1

# while success:
#     cv2.imwrite(f"images_from_video/{count}.jpg", frame)
#     print(f"images_from_video/{count}.jpg")
#     success, frame = video.read()
#     count += 1

#extract frame
time_to_extract = "00:00:02.75"
time_to_list = time_to_extract.split(':')
time_to_list_floats = [float(i) for i in time_to_list]
hours, minutes, seconds = time_to_list_floats


frame_time_seconds = (hours * 3600 + minutes * 60 + seconds)
frame_number = int(frame_time_seconds * fps)
print(f'frame #{frame_number}')

video.set(1, frame_number)
success, frame = video.read()

if success:
    cv2.imwrite(f"video_at_{time_to_extract}.jpg", frame)
else:
    print('time is out of range')
