# import package

```
import os

import cv2
```

# open the webcam

```
webcam=cv2.VideoCapture(0)
```

# stream the webcam

```
while True:
ret, frame = webcam.read()
if not ret:
break
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
```

# release the webcam

```
webcam.release()

cv2.destroyAllWindows()
```

[]: # (end)
