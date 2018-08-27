import pymeanshift as pms
import numpy as np
import cv2
import math
from PIL import Image, ImageStat
import sys
from os import listdir


def main():
    RED = 0
    GREEN = 1
    BLUE = 2
    #input_image = Image.open(sys.argv[1]+".png")
    path1 = "/Users/caijieyang/Desktop/Nice/Original_image/Transit1"
    files= listdir(path1)
    for file in files:
        if ".png" in file:
            bright_1=brightness_1(file)
            bright_2=brightness_2(file)
            bright_3=brightness_3(file)
            H,S,V= hsv(file)
            print file , bright_1, bright_2, bright_3, H,S,V

def brightness_1( im_file ):
    #Convert image to greyscale, return average pixel brightness. 
    im = Image.open(im_file).convert('L')
    area = (0, 0, 832, 208)
    cropped_img = im.crop(area)
    stat = ImageStat.Stat(cropped_img)
    return stat.mean[0]

def brightness_2( im_file ):
    #Convert image to greyscale, return RMS pixel brightness.
    im = Image.open(im_file).convert('L')
    area = (0, 0, 832, 208)
    cropped_img = im.crop(area)
    stat = ImageStat.Stat(cropped_img)
    return stat.rms[0]


def brightness_3( im_file ):
    #Average pixels, then transform to "perceived brightness".
    im = Image.open(im_file)
    area = (0, 0, 832, 208)
    cropped_img = im.crop(area)
    stat = ImageStat.Stat(cropped_img)
    #print "#######", stat.mean
    r,g,b,p = stat.mean
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

def hsv( im_file ):
    im = Image.open(im_file)
    area = (0, 0, 832, 208)
    cropped_img = im.crop(area)
    img = np.array(cropped_img)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(HSV)
    #H = HSV[:,:,0]
    #S = HSV[:,:,1].mean
    #V = HSV[:,:,2].mean
    #return H,S,V
    H=np.mean(H)
    S=np.mean(S)
    V=np.mean(V)
    return H,S,V



main()