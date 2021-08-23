import cv2
import os
import numpy as np
from os.path import isfile, join

pathIn = 'C:\\Users\\Mislab\\Desktop\\medical\\MF\\COVID-CT-master\\Images-processed\\CT_COVID\\'
pathOut = 'C:\\Users\\Mislab\\Desktop\\COVID\\'

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

print(len(files))

for i in range(len(files)):
    filename = pathIn + files[i]
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    filenameout = pathOut + files[i]
    cv2.imwrite(filenameout+str(i)+'.jpg', img)
