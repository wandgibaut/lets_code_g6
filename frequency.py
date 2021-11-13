import numpy as np
import pandas as pd

class Frequency:

    def __init__(self, data:pd.DataFrame):
        self.data = data.select_dtypes(np.object_)
        self.columns = self.data.columns
    
    def get_frequency(self, column: str = 'column') -> pd.DataFrame:
        
        print (column not in self.columns)
        if column not in self.columns:
            raise Exception("ColumnNotIsQualitative")

        self.frequency = pd.DataFrame()
        self.serie = self.data[column]
        self.__absolute__()
        self.__relative__()
        self.__absolute_accumulated__()
        self.__relative_accumulated__()
        return self.frequency
        
    def __absolute__(self) -> None:
        self.frequency['Absolute'] = self.serie.value_counts()
    
    def __relative__(self) -> None:
        self.frequency['Relative'] = self.frequency['Absolute']/self.serie.count()
    
    def __absolute_accumulated__(self) -> None:
        self.frequency['Absolute accumulated'] = self.frequency['Absolute'].cumsum()
        
    def __relative_accumulated__(self) -> None:
        self.frequency['Relative accumulated'] = self.frequency['Relative'].cumsum()
        
