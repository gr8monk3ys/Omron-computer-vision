import pandas as pd
import numpy as np

class History:
    def __init__(self):
        self.history = pd.DataFrame(columns=['partid','image','orientation','classification','metadata'])

    def addPart(self,partid:int,orientation:int,img:np.array)->None:
        d_row = pd.DataFrame({'partid':partid,'image':[img],'orientation':orientation,'classification':pd.NA,'metadata':pd.NA},columns=['partid','image','orientation','classification','metadata'])
        self.history = pd.concat(objs=[self.history,d_row],ignore_index=True)
    
    def removePart(self,partid)->None:
        if len(self.history[self.history['partid']==partid].index) > 0:
            self.history = self.history.drop(self.history[self.history['partid']==partid].index[-1]) # only delete most recent partid
    
    def saveHistory(self,path:str)->None:
        self.history.to_pickle(path)
    
    def loadHistory(self,path:str)->None:
        self.history = pd.read_pickle(path)
        
    def saveCSV(self,path:str)->None:
        self.history[['partid','orientation','classification']].to_csv(path,index=False)