from numpy import where
import matplotlib.pyplot as plt
import pandas as pd


class Helper():

    @staticmethod
    def add_new_row(data: pd.DataFrame, function_to_apply=lambda x: x, name: str = 'new row') -> pd.DataFrame:
        new_row = {}
        for column in data:
            new_row[column] = function_to_apply(data[column])
        return data.append(pd.Series(new_row, name=name))

    '''
    This is an implementation of John Tukey's definition of Outlier, or "Tukey's fences". 
    The formula is as follows:
    {\big [}Q_{1}-k(Q_{3}-Q_{1}),Q_{3}+k(Q_{3}-Q_{1}){\big ]}

    More information can be found here:
    [EN] https://en.wikipedia.org/wiki/Outlier#Tukey's_fences
    [PT-BR] https://pt.wikipedia.org/wiki/Outlier
    '''
    @staticmethod
    def replace_outliers(data: pd.DataFrame, replace_values: pd.Series, k: float = 1.5, quantile: float = 0.25) -> pd.DataFrame:
        lower_bound, upper_bound = Helper.get_lower_n_upper_bound(data, k, quantile)

        outliers_low = (data < lower_bound)
        outliers_high = (data > upper_bound)
        
        new_df = data.copy()
        new_df.mask(outliers_low, replace_values, inplace=True, axis=1)
        new_df.mask(outliers_high, replace_values, inplace=True, axis=1)

        return new_df

    @staticmethod
    def get_lower_n_upper_bound(data: pd.DataFrame,  k: float = 1.5, quantile: float = 0.25) -> pd.DataFrame:
        qr = data.quantile(1-quantile) - data.quantile(quantile)
        lower_bound = data.quantile(quantile) - k*qr
        upper_bound = data.quantile(1-quantile) + k*qr
        return lower_bound, upper_bound

    @staticmethod
    def boxplot(*argv, column_name: str = 'Total Household Income', **kwargs) -> None:
        fig, axs = plt.subplots(1, len(argv), figsize=(10, 5))
        fig.suptitle(f'Distribuição de Valores da coluna "{column_name}"')

        for i in range(len(argv)):
            data = argv[i][0]
            title = argv[i][1]
            axs[i].boxplot(data[column_name])
            axs[i].set_title(title)
    def means_data_per_income(data: pd.DataFrame, dummies_data: pd.DataFrame, col_income: str = 'Total Household Income', k: float = 10) -> pd.DataFrame:
        
        data_=data.copy()
        col_ref='Income Reference'
        
        quantile_ref =(100-k)/100 # list reference sorted data
        income_ref = data_[col_income].quantile(quantile_ref)        
        k_ref_mask = data_[col_income] > income_ref
        
        data_.loc[k_ref_mask, col_ref] = f'The {k:0.2f}% richest'
        data_.loc[(~k_ref_mask), col_ref] = 'Remainder'
        
        data_[dummies_data.columns]=dummies_data
        
        return pd.pivot_table(data_, index=col_ref)

