from History import History
from Pipeline import Pipeline
from picamera import PiCamera
from PIL import Image
import numpy as np
import cv2 as cv
from io import BytesIO
import matplotlib.pyplot as plt 

class Interface:
    def __init__(self):
        self.hist = History()
        self.clf = Pipeline()
        self.cam = PiCamera()
        
    def takePicture(self,partid:str,orientation:str):
        stream = BytesIO()
        self.cam.capture(stream,'png')
        stream.seek(0)
        im = Image.open(stream)
        im = np.asarray(im)
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        self.hist.addPart(partid,orientation,im)
        return im
        
    def saveCSV(self): 
        self.hist.saveCSV("history.csv")

    def classify_img(self,partid:str,orientation:str):
        res = self.clf.classify([self.hist.getImage(partid,orientation)])[0]
        self.hist.classifyPart(partid,orientation,res,np.NaN)
        return res
