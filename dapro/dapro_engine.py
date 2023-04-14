from dapro.data_importing import pro_import
from dapro.data_eda import pro_eda
from dapro.data_viz import pro_dataviz
from .input import get_data_file_path
import json


class DataProcessing:
    def __init__(self):
        with open(get_data_file_path("config/hyperparameter.json"), "rb") as f:
            parameters = json.load(f)
        self.bin_val = parameters['bin']

    @staticmethod
    def read_file(path):
        df = pro_import.DataImporting(path).data_import()
        return df

    @staticmethod
    def show_number_rows_cols(dataframe):
        rows, cols = pro_eda.DataEDA(dataframe).data_eda()
        return rows, cols

    @staticmethod
    def show_hist_plot(self, series):
        return pro_dataviz.DataViz(series).plot_histogram(self.bin_val)
