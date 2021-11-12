from numpy import double, where
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

        new_df = pd.DataFrame()
        for column in data:
            new_df[column] = where(data[column] >upper_bound[column], replace_values[column], data[column])
            new_df[column] = where(data[column] <lower_bound[column], replace_values[column], new_df[column])

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
        #fig.set_label('fig')

        for i in range(len(argv)):
            data = argv[i][0]
            title = argv[i][1]
            axs[i].boxplot(data[column_name])
            axs[i].set_title(title)
