# Linear Regression Model

### Concepts Implemented
- _Stochastic Gradient Descent_
  - The process of iteratively updating the parameters (weights and the bias term), such that you minimize your cost function, and reach it's global minima.
- _Cost Functions_
  - Using mean squared error to calculate the error in your current predictions, against the target values.
- _Feature Scaling Using Zscore Normalization_
  - Important for normalizing features and making sure they are all in a similar range, and can get weights assigned to them accordingly.
- _Regularization_
  - The process of slightly minimizing your parameters, such that your model does not overfit to the training data and hinder it's ability to generalize.
- _Learning Rate Selection_
  - Very crucial, as picking a value too small can significantly increase the training time, which can increase computational and overhead costs. Whereas, choosing a value to large, can cause the cost function to oscillate throughtout iterations of the gradient descent, and ultimately diverge, instead of converging to the global minima.
- _Lambda Selection_
  - Picking a value too small can bring no change, and leave the problem of overfitting unadressed. However, picking a value too large, will minimize the parameters too much, leading to underfitting, where the model performs poorly on both training and test data.
