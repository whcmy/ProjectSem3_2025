import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class LSTMTimeSeriesModel:
    def prepare_data(self, data, window_size=3):
        X, y = [], []
        for i in range(len(data) - window_size):
            X.append(data[i:i+window_size])
            y.append(data[i+window_size])
        X = np.array(X).reshape(-1, window_size, 1)
        y = np.array(y)
        return X, y

    def build_and_train(self, X, y):
        model = Sequential()
        model.add(LSTM(32, input_shape=(X.shape[1], 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        model.fit(X, y, epochs=50, verbose=0)
        return model
