import cv2
import os
import numpy as np

frame = 0

for frame in range(601):
    mask = cv2.imread('mask/arrow/' + str(frame).zfill(5) + '.png')
    mask[mask > 0] = 255
    # for white mask
    #mask[np.where((mask == [0, 0, 128]).all(axis=2))] = [255, 255, 255]

    img = cv2.imread('image/arrow/' + str(frame).zfill(5) + '.jpg')

    result = cv2.bitwise_or(img, mask)
    test_path = os.path.join('result/arrow')
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    cv2.imwrite('result/arrow/' + str(frame).zfill(5) + '.jpg', result)
