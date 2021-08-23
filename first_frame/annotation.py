import cv2
import os

image = cv2.imread('arrow/00000.jpg')
image = cv2.resize(image, (854, 480), interpolation=cv2.INTER_AREA)
cv2.imwrite(os.path.join('annotation', '00000.jpg'), image)
