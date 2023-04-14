import pandas as pd


class DataEDA:
    """
    Create 'DataEDA' class for the sub-package 'pro_eda'. In this example, we implement one method for data
    exploration 'data_shape'
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def data_shape(self):
        """
        Get dataframe
        :return: number of rows and columns
        """
        rows, cols = self.dataframe.shape
        return rows, cols
