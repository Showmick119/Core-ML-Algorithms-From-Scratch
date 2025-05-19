import numpy as np

class MyLinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000, normalize=True):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.normalize = normalize
        self.loss_history = []
        self.parameter_history = []
        self.weights = None
        self.bias = None

    def fit(self, X, y) -> None:
        x = 2

    def predict(self, X: np.ndarray) -> np.ndarray:
        m = X.shape[0]
        y_pred = np.zeros((m,))

        if self.normalize == True:
            X_norm = self._normalize_features(X)

        for i in range(m):
            y_pred[i] = np.dot(X_norm[i][:], self.weights) + self.bias

        return y_pred

    def _compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        cost = 0
        y_pred = self.predict(X)
        m = y_pred.shape[0]

        for i in range(m):
            cost += (y_pred[i] - y[i]) ** 2
        cost *= (1 / 2 * m)

        return cost

    def _compute_gradient(self, X: np.ndarray, y: np.ndarray) -> float:
        x = 2

    def _gradient_descent(self, X, y) -> float:
        x = 2
    
    def _normalize_features(self, X: np.ndarray) -> np.ndarray:
        self.column_std = np.std(X, axis=0)
        self.column_mean = np.mean(X, axis=0)

        return (X - self.column_mean) / (self.column_std)