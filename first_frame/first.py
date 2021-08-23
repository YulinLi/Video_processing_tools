import cv2
import os
import numpy as np

vidcap = cv2.VideoCapture('TPE_DENG_YU_CHENG.mp4')
success, image = vidcap.read()

if success:
    print('sc')
    image = cv2.resize(image, (842, 480), interpolation=cv2.INTER_AREA)
    cv2.imwrite("first_frame.jpg", image)
else:
    print('fail')
