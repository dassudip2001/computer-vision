# import all package

import os
import cv2

- read the path

img=os.path.join('data', 'data', 'video.jpg')

- read the image

cv2.imread(img)

- write the image

cv2.imwrite('data/data/video.jpg', img)

- show the image

cv2.imshow('image', img)

- wait for the user to press any key

cv2.waitKey(0)

- destroy all windows
  cv2.destroyAllWindows()
