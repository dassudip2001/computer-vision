# import package

- os

```import os

```

- import computer vision

```import cv2

```

- read the path

```video_path = os.path.join('data', 'data', 'video.jpg')

```

- read the video

```img = cv2.imread(video_path)

```

- show the image

```cv2.imshow('image', img)

```

- wait for the user to press any key

```cv2.waitKey(0)

```
