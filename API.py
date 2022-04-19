from History import History
from Pipeline import Pipeline
from Camera import Camera # or rpiCamera for picamera

import numpy as np

class Interface:
    def __init__(self):
        self.hist = History()
        self.clf = Pipeline()
        self.cam = Camera()
        
    def takePicture(self,partid:str,orientation:str):
        im = self.cam.takePicture()
        self.hist.addPart(partid,orientation,im)
        return im
        
    def saveCSV(self): 
        self.hist.saveCSV("history.csv")

    def classify_img(self,partid:str,orientation:str):
        res = self.clf.classify([self.hist.getImage(partid,orientation)])[0]
        self.hist.classifyPart(partid,orientation,res,np.NaN)
        return res
