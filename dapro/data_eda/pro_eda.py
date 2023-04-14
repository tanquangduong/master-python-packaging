import pandas as pd


class DataEDA:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def data_eda(self):
        """
        Get dataframe
        :return: number of rows and columns
        """
        rows, cols = self.dataframe.shape
        return rows, cols
