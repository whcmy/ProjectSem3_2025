import numpy as np
from sklearn.linear_model import LinearRegression

class LinearRegressionModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, data):
        X = np.arange(len(data)).reshape(-1, 1)
        y = np.array(data)
        self.model.fit(X, y)
        return self.model.coef_[0], self.model.intercept_

    def predict_future(self, data, steps=12):
        start = len(data)
        future_X = np.arange(start, start + steps).reshape(-1, 1)
        return self.model.predict(future_X)

