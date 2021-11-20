import numpy as np
import pandas as pd


class Frequency:

    def __init__(self, data: pd.DataFrame, columns=pd.Series):
        self.data = data
        self.columns = columns

    def show(self):

        report = {}

        for column in self.columns:

            report[column] = self._get_frequency(column)

        return report

    def _get_frequency(self, column: str = 'column') -> pd.DataFrame:

        if column not in self.columns:
            raise Exception("ColumnNotIsQualitative")

        self.frequency = pd.DataFrame()
        self.serie = self.data[column]
        self.frequency['Absolute'] = self._absolute()
        self.frequency['Relative'] = self._relative()
        self.frequency['Absolute accumulated'] = self._absolute_accumulated()
        self.frequency['Relative accumulated'] = self._relative_accumulated()
        return self.frequency

    def _absolute(self) -> pd.Series:
        return self.serie.value_counts()

    def _relative(self) -> pd.Series:
        return self.serie.value_counts(normalize=True)

    def _absolute_accumulated(self) -> pd.Series:
        return self.frequency['Absolute'].cumsum()

    def _relative_accumulated(self) -> pd.Series:
        return self.frequency['Relative'].cumsum()
