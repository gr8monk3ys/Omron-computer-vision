import pandas as pd
import numpy as np

class History:
    def __init__(self):
        self.history = pd.DataFrame(columns=['partid','image','orientation','classification','metadata'])

    def addPart(self,partid:int,orientation:int,img:np.array)->None:
        if len(self.history[(self.history['partid']==partid) & \
                            (self.history['orientation']==orientation)].index) == 0:
            d_row = pd.DataFrame({'partid':partid,
                                  'image':[img],'orientation':orientation,
                                  'classification':pd.NA,
                                  'metadata':pd.NA},
                                  columns=['partid','image','orientation','classification','metadata'])
            self.history = pd.concat(objs=[self.history,d_row],
                                     ignore_index=True)
        else:
            self.history.loc[(self.history['partid']==partid) & \
                             (self.history['orientation']==orientation),'image'] = [img]
            self.history.loc[(self.history['partid']==partid) & \
                             (self.history['orientation']==orientation),'classification'] = np.NAN
            self.history.loc[(self.history['partid']==partid) & \
                             (self.history['orientation']==orientation),'metadata'] = np.NAN
    
    def removePart(self,partid:int,orientation:int)->None:
        if len(self.history[self.history['partid']==partid].index) > 0:
            self.history = self.history.drop(self.history[(self.history['partid']==partid) & (self.history['orientation']==orientation)].index[-1]) # only delete most recent partid-orientation pair
            self.history = self.history.reset_index(drop=True)
            
    def classifyPart(self,partid:int,orientation:int,classification:int,metadata)->None:
        self.history.loc[(self.history.partid==partid) & \
                         (self.history.orientation==orientation),
                         'classification'] = classification
        self.history.loc[(self.history.partid==partid) & \
                         (self.history.orientation==orientation),
                         'metadata'] = metadata
    def getImage(self,partid:int,orientation:int)->np.array:
        return self.history[(self.history.partid==partid) & (self.history.orientation==orientation)]['image'].iloc[0]
    
    def saveHistory(self,path:str)->None:
        self.history.to_pickle(path)
    
    def loadHistory(self,path:str)->None:
        self.history = pd.read_pickle(path)
        
    def saveCSV(self,path:str)->None:
        self.history[['partid','orientation','classification']].to_csv(path,index=False)