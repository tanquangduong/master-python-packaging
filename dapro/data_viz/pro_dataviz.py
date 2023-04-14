import matplotlib.pyplot as plt
import seaborn as sns


class DataViz:
    """
    Create 'DataViz' class for the sub-package 'pro_eda'. In this example, we implement one method for data
    exploration 'plot_histogram'
    """
    def __init__(self, series):
        self.series = series

    @staticmethod
    def _histogram(series, bin_val):
        """
        Unit function to plot histogram for numerical feature
        :param series: feature as 'series' dtype from dataframe
        :param bin_val: Number of bin in histogram
        :return: figure of histogram
        """
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.hist(series,
                bins=bin_val,
                color='green',
                edgecolor="black",
                alpha=0.7)
        ax.set_title("Histogram with bin = {}".format(bin_val),
                     fontdict={
                         'fontsize': 15,
                         'fontweight': 'bold'
                     })
        ax.set_xlabel('Values',
                      fontsize=15,
                      fontweight='bold')
        ax.set_ylabel('Count',
                      fontsize=15,
                      fontweight='bold')
        # Hide the right and top spines
        ax.spines[['right', 'top']].set_visible(False)

    def plot_histogram(self, bin_val):
        """
        Get a series from the parent class and plot histogram
        :param bin_val: Number of bin in histogram
        :return: Figure of histogram
        """
        return self._histogram(self.series, bin_val)
