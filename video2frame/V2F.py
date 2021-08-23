import cv2
import os
import numpy as np
video = "43536"
vidcap = cv2.VideoCapture('output/' + video + ".mp4")
success, image = vidcap.read()
save = 'frame/' + video 

count = 0
while success:
    image = cv2.resize(image, (640, 400), interpolation=cv2.INTER_AREA)
    try:
        os.stat(save)
    except:
        os.mkdir(save)
    cv2.imwrite(os.path.join(save + '/', '%05d.jpg') %
                count, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
