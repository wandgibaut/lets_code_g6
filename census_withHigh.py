# High_income class - projeto pandas - Santander Coders 2021 - G6 (by Samya)
# Subset of Database object based on above 90th INCOME

import os
import pandas as pd
import census_database as census

class High_income(census.Database):

    def __init__(self):
        census.Database.__init__(self)
        self.data_highincome = self._subset_highincome()
        self._save2csv()
        print('High Income Data READY!')

    def _check_highincome(self): #create mask for High Income (10% top values)
        income_thresh = self.data['Total Household Income'].quantile(0.9)
        
        is_highincome = self.data['Total Household Income'] >= income_thresh
        return is_highincome
    
    def _subset_highincome(self): 
        is_highincome = self._check_highincome()
        
        newdata = self.data[is_highincome].copy()
        data_highincome = newdata.sort_values(by='Total Household Income', ascending=False)
        return data_highincome
        
    def _save2csv(self):
        fileout = os.path.join('output_files','High_Income_CensusData.csv')
        self.data_highincome.to_csv(fileout)
    