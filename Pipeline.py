from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import pickle
import numpy as np
import cv2 as cv
import pandas as pd

class NoModelFound:
    pass

class Pipeline:
    def __init__(self):
        # load pipeline
        try:
            with open('../model.pkl','rb') as file:
                self._pipe = pickle.load(file)
        except:
            raise NoModelFound
        # qual functions
        self._flatten = lambda batch : batch.reshape(batch.shape[0],-1)
    
    def classify(self,imgs):
        # classify single image using pipeline
        return self._pipe.predict(self._flatten(imgs))
    
    