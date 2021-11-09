# census_database class - projeto pandas - Santander Coders 2021 - G6 (by Samya)

class database():
    
    def __init__(self):
        self.data = self._readmerge_files() #create database
        self._quanti_vars() #create attribute QUANTITATIVE var
        self._quali_vars() #create attribute QUANLITATIVE var
        print('Census data READY!')
    
    ## methods for object initialization ###################
    def _list_files(self):
        import os
        arquivos = sorted([i for i in os.listdir() if i[-3:] == 'csv']) #check files in local dir
        return arquivos[0:3]
    
    def _readmerge_files(self):
        import pandas as pd
        self.arquivos = self._list_files() #list of files with census data
        
        data = pd.DataFrame()
        for file in self.arquivos:
            columns_data = set(data.columns) #columns in data
            
            file_content = pd.read_csv(file, delimiter = ';') #read file content
            file_columns = set(file_content.columns) #columns in new data
            
            common_columns = columns_data.intersection(file_columns) #find common columns
            are_commun_columns = len(common_columns) > 0 #are there common columns?
            
            if not are_commun_columns:
                data = pd.concat([data, file_content], axis = 1) #If not = concat by columns
            else:
                data = data.merge(file_content, on = list(common_columns)) #If does, concat on those
        
        return data
    
    def _quanti_vars(self): #check quantitative variables in columns
        data = self.data
        quanti = data._get_numeric_data().columns
        quanti = quanti.drop(['ID', 'Electricity'])
        self.quanti = set(quanti)
    
    def _quali_vars(self): #check qualitative variables in columns
        data = self.data
        columns = set(data.columns)
        quali = columns - self.quanti - {'ID'}
        self.quali = quali