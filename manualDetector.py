import os
# import gc
import cv2 as cv
import numpy as np

''' Testing for the images given to us manually '''

# Loading in specific images
img1 = cv.imread('Images/good_images/Left_side2.jpg', 0)
img2 = cv.imread('Images/bad_images/Missing_label1.jpg', 0)

# Resizing images
img1 = cv.resize(img1, (0, 0), fx = 0.1, fy = 0.1)
img2 = cv.resize(img2, (0, 0), fx = 0.1, fy = 0.1)

orb = cv.ORB_create(nfeatures = 1000)

# Finding the key features
key_point1, descriptor1 = orb.detectAndCompute(img1, None)
key_point2, descriptor2 = orb.detectAndCompute(img2, None)

# img_key_point1 = cv.drawKeypoints(img1, key_point1, 1)

# Matching the key features
bf = cv.BFMatcher()
matches = bf.knnMatch(descriptor1, descriptor2, k = 2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(img1, key_point1, img2, key_point2, good, None, flags = 2)

# cv.imshow('img1', img1)
# cv.imshow('img2', img2)
cv.imshow('img3', img3)

cv.waitKey(0)

