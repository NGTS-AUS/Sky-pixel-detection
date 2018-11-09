import numpy as np
import cv2
import math
from PIL import Image, ImageStat
import sys
from os import listdir
import pymeanshift as pms
import os.path

# path1 = "/Users/caijieyang/Desktop/allgoodthinghere/"
# files= listdir(path1)
avg_recall=[]
avg_pre=[]
hsl_acc_list=[]
manual_acc_list=[]
file = sys.argv[1]
file = str(file)
# print (file)
origin = Image.open(file)
width, height = origin.size
area = (0, 0, width, 0.5*height)
image = origin.crop(area) # crop top half of the image
image.save(file+"_cropped.png")

original_image = cv2.imread(file+"_cropped.png")

(segmented_image, label_image, number_regions) = pms.segment(original_image, spatial_radius=7, 
                                                              range_radius=8, min_density=300)

counterclass_all={}
for j in range(0,len(label_image[0])):
    for i in range(0,len(label_image)):
        if label_image[i,j] in counterclass_all:
            counterclass_all[label_image[i,j]] +=1
        else:
            counterclass_all[label_image[i,j]] = 1
max=0

for i in counterclass_all:
	if counterclass_all[i]>max:
		max=counterclass_all[i]
		most_common_colour=i

origin=cv2.imread(file)

data = np.asarray(origin,dtype="int32")
RED = 2
GREEN = 1
BLUE = 0
for i in range (len(original_image)):
	for j in range (len(original_image[0])):
	    if label_image[i][j] == most_common_colour:
	    	data[i, j, GREEN] = 0
	    	data[i, j, RED] = 0
	    	data[i, j, BLUE] = 255
	    else:
	    	continue
result = Image.fromarray(data.astype(np.uint8))
b, g, r = result.split()
result = Image.merge("RGB", (r, g, b))
result.save(file+"ms_sky_mark.png")


ms = Image.fromarray(segmented_image)
b, g, r = ms.split()
im = Image.merge("RGB", (r, g, b))
im.save(file+"ms_cluster_mark.png")

tempfile = file.replace('.png',' - Copy.png')
if os.path.isfile(tempfile):
	marked_pixel_values = cv2.imread(tempfile)
	true_po_list=[]
	precision_list=[]

	true_sky_counter=0
	true_positive_counter=0
	false_positive_counter=0
	# print (marked_pixel_values[0,0])
	# print (int(len(marked_pixel_values)/2+1))
	for i in range(int(len(marked_pixel_values)/2+1)):
	    for j in range(len(marked_pixel_values[0])):
	        if marked_pixel_values[i][j][0] == 255 and marked_pixel_values[i][j][1] == 0 and marked_pixel_values[i][j][2] == 0 :
	            true_sky_counter+=1
	            if data[i][j][0] == 255 and data[i][j][1] == 0 and data[i][j][2] == 0:
	                true_positive_counter+=1
	        else:
	            if data[i][j][0] == 255 and data[i][j][1] == 0 and data[i][j][2] == 0:
	                false_positive_counter+=1
	avg_recall.append(true_positive_counter/true_sky_counter)
	avg_pre.append(true_positive_counter/(true_positive_counter+false_positive_counter))
	hsl_acc_list.append((true_positive_counter+false_positive_counter)/((len(marked_pixel_values)/2+1)*len(marked_pixel_values[0])))
	manual_acc_list.append(true_sky_counter/((len(marked_pixel_values)/2+1)*len(marked_pixel_values[0])))    
	print ("meanshift program marked proportion:", (true_positive_counter+false_positive_counter)/((len(marked_pixel_values)/2+1)*len(marked_pixel_values[0])))
	print ("manually marked proportion:",true_sky_counter/((len(marked_pixel_values)/2+1)*len(marked_pixel_values[0])))
# print ("recall: ", avg_recall)
# print ("precision: " , avg_pre)
# print ("recall: ", np.mean(avg_recall))
# print ("precision: " , np.mean(avg_pre))
# print (hsl_acc_list)
# print (manual_acc_list)
