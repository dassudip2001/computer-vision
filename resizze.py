import os  # import os module   

import cv2 # import opencv module

# Function to read image and resize it
def read_imag(path):
    img = cv2.imread(path)
    print("original size",img.shape)
    img1 = cv2.resize(img, (224, 224))
    print(img1.shape)
    cv2.imshow('resize image',img1)
    return img


show=read_imag('image.jpg') # read image and resize it
cv2.imshow('image',show) # show image
cv2.waitKey(0) # wait for key press

