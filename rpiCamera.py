from picamera import PiCamera

from PIL import Image
import numpy as np
import cv2 as cv
import io


class Camera:
    
    def __init__(self):
        self.cam = PiCamera()
        self.cam.shutter_speed = 0.5 # number of seconds for exposure
        
    def takePicture(self):
        stream = io.BytesIO()
        self.cam.capture(stream,'png')
        stream.seek(0)
        im = Image.open(stream)
        im = np.asarray(im)
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        return im
            