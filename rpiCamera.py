from picamera import PiCamera

from PIL import Image
import numpy as np
import cv2 as cv
import io
import time


class Camera:
    
    def __init__(self):
        self.cam = PiCamera()
        self.cam.shutter_speed = 5 # number of seconds for exposure
        
    def takePicture(self):
        #stream = io.BytesIO()
        #self.cam.capture(stream,'png')
        #stream.seek(0)
        
        self.cam.start_preview()
        time.sleep(1)
        self.cam.capture('/tmp/picture.jpg')
        self.cam.stop_preview()
        im = Image.open('/tmp/picture.jpg')
        im = np.asarray(im, dtype = np.float32)
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        return im
            