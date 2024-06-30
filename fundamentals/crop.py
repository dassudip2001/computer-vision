# import package
import os 
import cv2

image_path = 'image.jpg' # path of image

img=cv2.imread(image_path) # read image


# Function to crop image
def crop_image(image, start_x, start_y, end_x, end_y):
    crop_img = image[start_y:end_y, start_x:end_x] # crop image
    cv2.imshow("cropped", crop_img) # show cropped image
    cv2.waitKey(0) # wait for key press
    cv2.destroyAllWindows() # close all windows


crop_image(img, 50, 50, 200, 200) # crop image