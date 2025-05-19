import numpy as np

class MyLinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000, normalize=True):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.normalize = normalize
        self.weights = None
        self.bias = None

    def fit(self) -> None:
        x = 2

    def predict(self, X: np.ndarray) -> np.ndarray:
        m = X.shape[0]
        y_pred = np.zeros((m,))

        if self.normalize == True:
            X_norm = self._normalize_features(X)

        for i in range(m):
            y_pred[i] = np.dot(X_norm[i][:], self.weights) + self.bias

        return y_pred

    def _compute_cost(self, X, y) -> float:
        m, n = X.shape
        y_pred = self.predict(X)

    def gradient_descent(self) -> float:
        x = 2
    
    def _normalize_features(self, X: np.ndarray) -> np.ndarray:
        self.column_std = np.std(X, axis=0)
        self.column_mean = np.mean(X, axis=0)

        return (X - self.column_mean) / (self.column_std)