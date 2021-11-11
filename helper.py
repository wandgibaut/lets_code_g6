import pandas as pd


class Helper():

    @staticmethod
    def add_median_row(data: pd.DataFrame) -> pd.DataFrame:
        median_row = {}
        for column in data:
            median_row[column] = data[column].median()
        return data.append(pd.Series(median_row, name='median'))
