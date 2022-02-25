import os
# import gc
import cv2 as cv
import numpy as np

''' Testing for the images given to us '''

# Establishing image path
prod_good_dir = r'Images/good_images/'
prod_bad_dir = r'Images/bad_images/'

orb = cv.ORB_create()

# Iterating over all files and getting string names of images
images = []
img_list = os.listdir(prod_good_dir) + os.listdir(prod_bad_dir)
for cl in img_list:
    img_cur = cv.imread(f'{path}/{cl}', 0)
    images.append(img_cur)

# Finding descriptors for each of the images
def findDescriptor(images):
    des_list = []
    for img in images:
        key_point, descriptor = orb.detectAndCompute(img, None)
        des_list.append(descriptor)
        return des_list

des_ist = findDescriptor(images)

# Identifying each of the 
def findID(img, des_list, threshold = 20):
    key_point2, descriptor2 = orb.detectAndCompute(img, None)
    bf = cv.BFMatcher(nfeatures = 1000)
    match_list = []
    final_val = -1

    # Brute force matching
    try:
        for des in des_ist:
            matches = bf.knnMatch(descriptor, descriptor2, k = 2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            match_list.append(len(good))
    except:
        pass

    max_match = max(match_list)
    if(len(match_list)) != 0:
        if max_match > threshold:
            final_val = match_list.index(max_match)
    return final_val

''' Testing with live video footage '''

# cap = cv.VideoCapture(0)

# while True:
#     success, img2 = cap.read()
#     img_original = img2.copy()
#     img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

#     id = findID(img2, des_list)
#     if id != -1:
#         cv.putText(img_original, text, (50, 50), cv.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 2)

#     cv.imshow('img2', img_original)
#     cv.waitKey(1)
