import matplotlib.pyplot as plt

class ModelEvaluation:
    def plot_comparison(self, true_values, predicted_values, title):
        plt.plot(true_values, label="True", marker='o')
        plt.plot(predicted_values, label="Predicted", marker='x')
        plt.title(title)
        plt.xlabel("Time Index")
        plt.ylabel("Humidity (%)")
        plt.legend()
        plt.grid()
        plt.show()
