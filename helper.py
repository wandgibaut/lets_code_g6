import pandas as pd


class Helper():

    @staticmethod
    def add_new_row(data: pd.DataFrame, function_to_apply=lambda x: x, name: str = 'new row') -> pd.DataFrame:
        new_row = {}
        for column in data:
            new_row[column] = function_to_apply(data[column])
        return data.append(pd.Series(new_row, name=name))
