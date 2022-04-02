from History import History
from Pipeline import Pipeline

from picamera import PiCamera
from PIL import Image

class Interface:
    def __init__(self):
        hist = History()
        clf = Pipeline()
        cam = PiCamera()
        
    def takePicture(self,partid:int,orientation:int):
        stream = BytesIO()
        cam.capture(stream,'png')
        stream.seek(0)
        im = Image.open(stream)
        hist.addPart(partid,orientation,im)
        
    def saveCSV(self): 
        hist.saveCSV("history.csv")

    def classify_img(self,partid:int,orientation:int):
        res = clf.classify([hist.getImage(partid,orientation)])[0]
        hist.classifyPart(partid,orientation,res)
