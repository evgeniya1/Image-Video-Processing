import cv2
import os

color_image = cv2.imread('galaxy.jpeg', 1)
grey_image = cv2.imread('galaxy.jpeg', 0)
cv2.imwrite('galaxy-grey.jpeg', grey_image)


#resize image
def resize(image_path, resize_percentage, resized_path):

  image = cv2.imread(image_path)
  width = int(image.shape[1] * resize_percentage)
  height = int(image.shape[0] * resize_percentage)
  resized_image = cv2.resize(image, (width, height))
  cv2.imwrite(image_path + '_resized', resized_image)


resize(image_path='galaxy.jpeg',
       resize_percentage=0.5,
       resized_path='galaxy_resized.jpeg')
