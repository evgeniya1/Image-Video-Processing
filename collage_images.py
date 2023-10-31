#%%
import cv2
import os
import numpy as np

columns = 3
rows = 2

horizontal_margin = 40
vertical_margin = 20

IMAGES_FOLDER = 'images_to_collage'
images = os.listdir(IMAGES_FOLDER)

shape = cv2.imread(IMAGES_FOLDER + '/' + images[0]).shape
print(images)
print(shape)

big_image = np.zeros((shape[0]*rows + vertical_margin*(rows + 1), 
                      shape[1]*columns + horizontal_margin*(columns + 1), 
                      shape[2]), np.uint8)

big_image.fill(255)

#cv2.imwrite('grid.jpeg', big_image)

positions = [(x, y) for x in range(columns) for y in range(rows)]
images = [cv2.imread(IMAGES_FOLDER + '/' + image) for image in images]
#add images
for coord, image in zip(positions[:1], images[:1]):
    x = coord[0] * (shape[1]+ vertical_margin) + vertical_margin
    y = coord[1] * (shape[0]+ horizontal_margin) + horizontal_margin

    print(image.shape)
    print('shape', shape)
    print(x, x+shape[1],y,y+shape[0])

    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite('grid.jpeg', big_image)
# %%
