from PIL import Image
import numpy as np
import cv2 as cv
import io

class Camera:
    def __init__(self):
        pass
    def takePicture(self):
        self.cam = cv.VideoCapture(0)
        _, im = self.cam.read()
        self.cam.release()
        im = np.asarray(im)
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        return im
