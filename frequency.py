import numpy as np
import pandas as pd

class Frequency:

    def __init__(self, data:pd.DataFrame):
        self.data = data.select_dtypes(np.object_)
        self.columns = self.data.columns
    

    def show(self):
        
        report = {}
        
        for column in self.columns:

            report[column] = self.__get_frequency__(column)
            

        return report


    def __get_frequency__(self, column: str = 'column') -> pd.DataFrame:
        
        if column not in self.columns:
            raise Exception("ColumnNotIsQualitative")

        self.frequency = pd.DataFrame()
        self.serie = self.data[column]
        self.frequency['Absolute'] = self.__absolute__()
        self.frequency['Relative'] = self.__relative__()
        self.frequency['Absolute accumulated'] = self.__absolute_accumulated__()
        self.frequency['Relative accumulated'] = self.__relative_accumulated__()
        return self.frequency
        
    def __absolute__(self) -> pd.Series:
       return self.serie.value_counts()
    
    def __relative__(self) -> pd.Series:
        return self.frequency['Absolute']/self.serie.count()
    
    def __absolute_accumulated__(self) -> pd.Series:
        return self.frequency['Absolute'].cumsum()
        
    def __relative_accumulated__(self) -> pd.Series:
        return self.frequency['Relative'].cumsum()
        
