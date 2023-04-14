import pandas as pd


class DataImporting:
    """
    Create 'DataImporting' class for the sub-package 'pro_import'. In this example, we implement one method for data
    importation 'data_import'
    """
    def __init__(self, path):
        self.path = path

    def data_import(self):
        """
        Get data path of csv file, read csv file using pandas package
        :return: dataframe
        """
        return pd.read_csv(self.path)
