
"""
Created on Fri Feb 11 22:19:06 2022
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



class DataOperations():
    
    # class başlangıç fonksiyonu
    def __init__(self,data="Random"):
        
        self.data = str(data)

        # eğer np.array 
        if isinstance(self.data, np.ndarray):
            self.data = pd.DataFrame(self.data)
        
        # eğer DataFrame
        elif isinstance(self.data, pd.core.frame.DataFrame):
            pass
            
    
        # eğer csv path i ise
        elif ".csv" in self.data:
            self.data = pd.read_csv(self.data)
            
        
        # eğer json path i ise
        elif ".json" in self.data:
            self.data = pd.read_json(self.data)
            

        # eğer input verilmezse
        elif self.data == "Random":
            self.data = np.random.randint(20,100,15)
            self.data = self.data.reshape(5,3)
            self.data = pd.DataFrame(self.data,columns=["kolon_1","kolon_2","kolon_3"])
            


    def desci(self):
        # describe 
        desc = self.data.describe()
        print(desc)
    
    
    def visual(self):
        
        # sadece numerik olan kolonlardan  bir df oluştur
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        newdata = self.data.select_dtypes(include=numerics)

        # bütün  sayısal kolonların grafiğini çizdir
        columns = newdata.columns
        for column in columns:
            sns.distplot(newdata[column])
            plt.show()

