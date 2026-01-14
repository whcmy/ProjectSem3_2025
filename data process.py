analog_values = [80,85,90,92,95,97,100,102,104,106,108,110,112,114,116,118,120,122,124,126]
humidity_values = [73.7,71.1,68.4,67.4,65.8,64.7,63.2,62.1,61.1,60.0,
                   59.0,57.9,56.8,55.8,54.7,53.7,52.6,51.6,50.5,49.5]


import numpy as np

class DataDenoising:
    def __init__(self, window_size=3):
        self.window_size = window_size

    def moving_average(self, data):
        return np.convolve(data, np.ones(self.window_size)/self.window_size, mode='valid')


class DataNormalization:
    def normalize(self, data):
        min_val = np.min(data)
        max_val = np.max(data)
        return (data - min_val) / (max_val - min_val)


class DataStatistics:
    def describe(self, data):
        return {
            "mean": np.mean(data),
            "std": np.std(data),
            "min": np.min(data),
            "max": np.max(data)
        }


import matplotlib.pyplot as plt

class DataVisualization:
    def plot_time_series(self, data):
        plt.plot(data, marker='o')
        plt.xlabel("Time Index")
        plt.ylabel("Humidity (%)")
        plt.title("Soil Moisture Time Series")
        plt.grid()
        plt.show()



