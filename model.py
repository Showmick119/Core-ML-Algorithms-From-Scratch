import numpy as np
import math
from typing import Tuple

class MyLinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000, normalize=True):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.normalize = normalize
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if self.normalize == True:
            X_normalized = self._normalize_features(X)
        
        self.weights, self.bias = self._gradient_descent(X_normalized, y)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        m = X.shape[0]
        y_pred = np.zeros((m,))

        if self.normalize == True:
            X_normalized = self._normalize_features(X)
        else:
            X_normalized = X

        for i in range(m):
            y_pred[i] = np.dot(X_normalized[i][:], self.weights) + self.bias

        return y_pred

    def _compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        cost = 0.0
        y_pred = self.predict(X)
        m = y_pred.shape[0]

        for i in range(m):
            cost += (y_pred[i] - y[i]) ** 2
        cost *= (1 / 2 * m)

        return cost

    def _compute_gradient(self, X: np.ndarray, y: np.ndarray) -> Tuple[float, np.ndarray]:
        m, n = X.shape
        y_pred = self.predict(X)

        dj_db = 0.0
        dj_dw = np.zeros((n,))

        for i in range(m):
            dj_db += (y_pred[i] - y[i])
            for j in range(n):
                dj_dw[j] += (y_pred[i] - y[i]) * X[i][j]
        dj_db *= (1 / m)
        dj_dw *= (1 / m)

        return dj_db, dj_dw

    def _gradient_descent(self, X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, float]:
        n = X.shape[1]
        self.cost_history = []
        self.parameter_history = []
        self.weights = np.zeros(n)
        self.bias = 0.0

        for i in range(self.num_iterations):
            dj_dw, dj_db = self._compute_gradient(X, y)

            self.weights = self.weights - self.learning_rate * dj_dw
            self.bias = self.bias - self.learning_rate * dj_db

            self.cost_history.append(self._compute_cost(X, y))
            self.parameter_history.append((self.weights, self.bias))

            if i % math.ceil(self.num_iterations / 10) == 0:
                print(f"Iteration {i:4d}: Cost {self.cost_history[-1]:8.2f}")
        
        return self.weights, self.bias

    def _normalize_features(self, X: np.ndarray) -> np.ndarray:
        if not hasattr(self, 'column_mean'):
            self.column_std = np.std(X, axis=0)
            self.column_mean = np.mean(X, axis=0)

        return (X - self.column_mean) / (self.column_std)