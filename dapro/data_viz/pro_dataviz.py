import matplotlib.pyplot as plt
import seaborn as sns


class DataViz:
    def __init__(self, series):
        self.series = series

    def _histogram(self, bin_val):
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.hist(self.series,
                bins=bin_val,
                color='green',
                edgecolor="black",
                alpha=0.7)
        ax.set_title("Histogram example",
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
        Get a series
        :return: histogram plot
        """
        return self._histogram(bin_val)
