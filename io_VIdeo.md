# os

import os

- import computer vision

import cv2

- read the path

video_path = os.path.join('data', 'data', 'video.mp4')

- read the video

cap = cv2.VideoCapture(video_path)

- stram the video

```while True:
ret, frame = cap.read()
if not ret:
break
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break

```
