from dapro.data_importing import pro_import
from dapro.data_eda import pro_eda
from dapro.data_viz import pro_dataviz
from .input import get_data_file_path
import json
import os


class DataProcessing:
    """
    Create 'DataProcessing' class for 'dapro' package. In this example, we will create 3 methods:
    'read_file', 'show_number_rows_cols' and 'show_hist_plot'.
    This class allows to load hyperparameter as default in the package if config_path=None. In contrast,
    if config_path!=None, it can dynamically load new hyperparameter in Dev environment
    """
    def __init__(self, config_path=None):
        if config_path:
            with open(os.path.join(os.getcwd(), config_path)) as f:
                self.parameters = json.load(f)
        else:
            with open(get_data_file_path("config/hyperparameter.json"), "rb") as f:
                self.parameters = json.load(f)

    @staticmethod
    def read_file(path):
        """
        Call sub-package 'pro_import' to import dataframe from path
        :param path: dataset path
        :return: dataframe
        """
        df = pro_import.DataImporting(path).data_import()
        return df

    @staticmethod
    def show_number_rows_cols(dataframe):
        """
        Call sub-package 'pro_eda' to calculate basic Exploratory Data Analysis
        :param dataframe:
        :return: row number, column number
        """
        rows, cols = pro_eda.DataEDA(dataframe).data_shape()
        return rows, cols

    def show_hist_plot(self, series, bin_num=None):
        """
        Call sub-package 'data_viz' to plot histogram for a given array / series
        :param series: One of the columns under 'series' dtype
        :param bin_num: Number of bin in histogram. Default as '100'
        :return: Plot histogram
        """
        if not bin_num:
            bin_num = self.parameters['bin']
        return pro_dataviz.DataViz(series).plot_histogram(bin_num)
