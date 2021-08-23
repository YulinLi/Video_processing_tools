import cv2
import os
import numpy as np
import argparse
from os.path import isfile, join


def get_arguments():
    parser = argparse.ArgumentParser(description="SST")
    parser.add_argument("-s", type=str, help="seg, V2F, F2V", defult=seg)
    parser.add_argument("-f", type=str, help="foldername", default='none')
    parser.add_argument("-v", type=str, help="video name", default='none')
    return parser.parse_args()


args = get_arguments()

SET = args.s
foldername = args.f
videoname = args.v

if(SET == 'F2V'):

    pathIn = 'seg/result/' + foldername
    pathOut = 'F2V/' + videoname + '.mp4'
    fps = 16
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: x[5:-4])
    files.sort()
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: x[5:-4])
    for i in range(len(files)):
        filename = pathIn + files[i]
        print('filename:')
        print(filename)
        # reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)

        # inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'MPEG'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


elif(SET == 'V2F'):
    vidcap = cv2.VideoCapture('V2F/'+videoname)
    success, image = vidcap.read()

    count = 0
    while success:
        image = cv2.resize(image, (842, 480), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join('foldername', '%05d.jpg') %
                    count, image)     # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
else:
    frame = 0
    frame_number = sum([len(files)
                        for r, d, files in os.walk('seg/image/'+foldername)])

    for frame in range(frame_number):
        mask = cv2.imread('seg/mask/' + foldername +
                          str(frame).zfill(5) + '.png')
        mask[mask > 0] = 255
        # for white mask
        #mask[np.where((mask == [0, 0, 128]).all(axis=2))] = [255, 255, 255]

        img = cv2.imread('seg/image/' + foldername +
                         str(frame).zfill(5) + '.jpg')

        result = cv2.bitwise_or(img, mask)
        test_path = os.path.join('seg/result/' + foldername)
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        cv2.imwrite('seg/result/' + foldername +
                    str(frame).zfill(5) + '.jpg', result)
