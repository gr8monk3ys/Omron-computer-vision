import os
import numpy as np
import cv2 as cv
import glob
from PIL import Image, ImageOps

class OrientationNotFound(BaseException):
    pass

class Pipeline:
    def __init__(self):
        self.orb = cv.ORB_create()
        self.bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
        self._reshp = lambda image : cv.resize(image,(250,250))
        self.thresholds = {
            'left': (16.82223140495868, 5.347255779597739),
            'right': (18.00145124716553, 5.211317313204525),
            'back': (15.945124716553291, 4.71509139790261),
            'front': (18.788512396694216, 6.047826117346583)
        }
        self.coefs = {"top":0.65,"right":1.4,"left":0.65,"front":0.9,"back":.4}
    def classify(self,imgs:np.array, ori:str):
        
        res = list(map(lambda im : self.score(im,ori), np.array(list(map(self._reshp,imgs))) ))
        thresh = self.get_thresh(ori)
        cls = list(map(lambda r : int(r[0] - self.coefs[ori]*r[1] < thresh[0] + self.coefs[ori]*thresh[1]), res))
        return cls
    
    def get_ref(self,ori:str):
        if ori not in os.listdir("../dataset/reference/good/"):
            raise OrientationNotFound()
            
        ref = []
        reshp = lambda image : cv.resize(image,(250,250))
        for f in glob.iglob("../dataset/reference/good/{}/*".format(ori)):
            im = np.asarray(ImageOps.grayscale(Image.open(f)))
            im = reshp(im)
            ref.append(im)
        return ref
    
    def get_thresh(self,ori:str):
        if ori in self.thresholds:
            return self.thresholds[ori]
        res = self.get_ref(ori)
        ans = list(map(lambda im: self.score(im,ori),res[:])) # currently uses all reference images for threshold
        mean = np.mean(list(map(lambda r: r[0],ans)))
        std = np.mean(list(map(lambda r: r[1],ans)))
        self.thresholds[ori] = (mean,std)
        
        return mean, std
    
    def score(self,im:np.array, ori:str):
        ref = self.get_ref(ori)
        
        res = [self.orb.detectAndCompute(im1,None) for im1 in ref]
        kp2, des2 = self.orb.detectAndCompute(im,None)
        
        matches_meta = list(map(lambda x: sorted(self.bf.match(x[1],des2), key = lambda x:x.distance),res))
        score_meta = list(map(lambda match: np.mean(list(map(lambda x:x.distance,match[:50]))),matches_meta))
        
        score_avg = np.mean(score_meta)
        score_std = np.std(score_meta)
        
        return score_avg, score_std