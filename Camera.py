from PIL import Image
import numpy as np
import cv2 as cv
import io

class Camera:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
    def takePicture(self):
        _, im = self.cam.read()
        im = np.asarray(im)
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        return im