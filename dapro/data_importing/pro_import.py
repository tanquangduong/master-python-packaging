import pandas as pd


class DataImporting:
    def __init__(self, path):
        self.path = path

    def data_import(self):
        """
        Get data path of csv file
        :return: dataframe
        """
        return pd.read_csv(self.path)
