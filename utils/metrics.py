def mean_squared_error(y_true, y_pred):
    """
    MSE = (1 / m) * sum((y_pred - y_true) ** 2)
    """

def root_mean_squared_error(y_true, y_pred):
    """
    RMSE = sqrt(MSE)
    """

def mean_absolute_error(y_true, y_pred):
    """
    MAE = (1 / m) * sum(|y_pred - y_true|)
    """

def r2_score(y_true, y_pred):
    """
    R2 = 1 - sum((y_true - y_pred) ** 2) / sum((y_true - y_pred) ** 2) 
    """