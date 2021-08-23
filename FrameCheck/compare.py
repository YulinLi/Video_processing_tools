import cv2
import numpy as np
import os
from os.path import isfile, join

cur_video = 'arrow\\'
pointrend = "\\pointrend\\davis2017_resnet101_cfbi_davis_ckpt_22000\\Annotations\\480p\\"
no_IA = "\\pointcfbi_wo_IA\\"

pathCFBI = 'C:\\Users\\Mislab\\Desktop\\Research\\AVOS\\result\\vos_davis\\eval\\finetuned\\origin_cfbi\\Annotations\\480p\\' + cur_video
pathCFBIp = 'C:\\Users\\Mislab\\Desktop\\Research\\AVOS\\result\\vos_davis\\eval\\finetuned\\cfbip\\Annotations\\480p\\' + cur_video
pathResult = 'C:\\Users\\Mislab\\Desktop\\Research\\AVOS\\result\\vos_davis\\eval\\finetuned' + pointrend + cur_video
pathgt = 'C:\\Users\\Mislab\\Desktop\\davis17\\DAVIS\\Annotations\\480p\\' + cur_video
pathimg = 'C:\\Users\\Mislab\\Desktop\\davis17\\DAVIS\\JPEGImages\\480p\\' + cur_video
save = 'result'

cfbi_frames = [f for f in os.listdir(pathCFBI) if isfile(join(pathCFBI, f))]
cfbi_frames.sort(key=lambda x: x[5:-4])
cfbi_frames.sort()

"""cfbip_frames = [f for f in os.listdir(pathCFBIp) if isfile(join(pathCFBIp, f))]
cfbip_frames.sort(key=lambda x: x[5:-4])
cfbip_frames.sort()"""

my_frames = [f for f in os.listdir(pathResult) if isfile(join(pathResult, f))]
my_frames.sort(key=lambda x: x[5:-4])
my_frames.sort()

gt_frames = [f for f in os.listdir(pathgt) if isfile(join(pathgt, f))]
gt_frames.sort(key=lambda x: x[5:-4])
gt_frames.sort()

img_frames = [f for f in os.listdir(pathimg) if isfile(join(pathimg, f))]
img_frames.sort(key=lambda x: x[5:-4])
img_frames.sort()

for i in range(len(cfbi_frames)):
    filename = pathCFBI + cfbi_frames[i]
    cfbi_img = cv2.imread(filename)
    height, width, layers = cfbi_img.shape
    size = (width, height)

    filename = pathResult + cfbi_frames[i]
    my_img = cv2.imread(filename)

    """filename = pathCFBIp + cfbi_frames[i]
    CFBIp_img = cv2.imread(filename)"""

    filename = pathgt + cfbi_frames[i]
    gt_img = cv2.imread(filename)
    gt_img1 = gt_img
    gt_img2 = gt_img

    filename = pathimg + cfbi_frames[i][0:5] + '.jpg'
    jp_img = cv2.imread(filename)

    dif = np.full_like(my_img, 0)
    dif0 = np.full_like(my_img, 0)
    dif1 = np.full_like(my_img, 0)
    dif2 = np.full_like(my_img, 0)
    dif3 = np.full_like(my_img, 0)
    dif4 = np.full_like(my_img, 0)

    """dif = my_img + gt_img"""
    """dif[np.where(my_img < cfbi_img)] = 255
    dif0[np.where(my_img > cfbi_img)] = 255
    dif1[np.where(my_img < gt_img)] = 255
    dif2[np.where(my_img > gt_img)] = 255
    dif3[np.where(cfbi_img < gt_img)] = 255
    dif4[np.where(cfbi_img > gt_img)] = 255"""
    """dif3[np.where(my_img < cfbi_img)] = 255
    dif4[np.where(my_img > cfbi_img)] = 255"""
    #dif = gt_img1

    #dif1 = cfbi_img + gt_img
    """gt_img2[np.where(cfbi_img == gt_img)] = 0
    dif1 = gt_img2"""

    """dif[np.where(my_img != gt_img)] = 200
    dif1[np.where(cfbi_img != gt_img)] = 200"""
    #dif2[np.where(dif != my_img)] = 100
    #dif2[np.where(dif != dif1 )] = 100

    #dif[np.where(dif != gt_img)] = 0
    add = cv2.addWeighted(my_img, 0.5, jp_img, 0.5, 0)
    
    """dif = 0.7*dif + 0.3*jp_img
    dif0 = 0.7*dif0 + 0.3*jp_img
    dif1 = 0.7*dif1 + 0.3*jp_img
    dif2 = 0.7*dif2 + 0.3*jp_img
    dif3 = 0.7*dif3 + 0.3*jp_img
    dif4 = 0.7*dif4 + 0.3*jp_img"""
    """final = np.full_like(my_img, 0)
    final[np.where(gt_img == dif)] = 255"""
    # assert False
    #dif[np.where(my_img != dif)] = 255
    output0 = save+'\\'+cfbi_frames[i]
    #output = save+'\\'+cfbi_frames[i] + '_cut_cfbi_my' '.jpg'
    #output0 = save+'\\'+cfbi_frames[i] + '_add_cfbi_my' '.jpg'
    #output1 = save+'\\'+cfbi_frames[i] + '_miss_gt' + '.jpg'
    #output2 = save+'\\'+cfbi_frames[i] + '_more_gt' + '.jpg'
    #output3 = save+'\\'+cfbi_frames[i] + '_miss_cfbi' + '.jpg'
    #output4 = save+'\\'+cfbi_frames[i] + '_more_cfbi' + '.jpg'
    cv2.imwrite(output0,add)
    #cv2.imwrite(output,dif)
    #cv2.imwrite(output0,dif0)
    #cv2.imwrite(output1,dif1)
    #cv2.imwrite(output2,dif2)
    #cv2.imwrite(output3,dif3)
    #cv2.imwrite(output4,dif4)
