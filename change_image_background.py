import cv2
import numpy as np

#load images
foreground = cv2.imread('giraffe.jpeg')
background = cv2.imread('safari.jpeg')

print(foreground.shape)
print(background.shape)

resized_background = cv2.resize(background, (width, height))

width = foreground.shape[1]
height = foreground.shape[0]

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any((pixel) == [1,255,0]):
            foreground[j, i] = resized_background[j, i]

cv2.imwrite('giraffe_with_safari.jpeg', foreground)
