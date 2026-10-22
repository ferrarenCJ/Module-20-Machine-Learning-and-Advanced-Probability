import numpy as np


def model(w, x):
    """
    Linear prediction model

    y = w0 + w1*x
    """
    return np.dot(w, x)


def grad_mse(w, xy):
    """
    Gradient of the Mean Squared Error
    """

    (x, y) = xy

    # Compute predictions
    ypredicted = model(w, x)

    # Difference between actual and predicted values
    diff = y - ypredicted

    # Compute gradient
    grad = -np.dot(x, diff)

    return grad


def mse(w, xy):
    """
    Mean Squared Error Loss Function
    """

    (x, y) = xy

    xt = np.transpose(x)

    ypredicted = np.dot(w, x)

    loss = np.sum((y - ypredicted) * (y - ypredicted))

    m = 2 * len(y)

    loss = loss / m

    return loss