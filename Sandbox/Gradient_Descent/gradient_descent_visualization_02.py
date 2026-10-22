import numpy as np
import matplotlib.pyplot as plt
import time

plt.style.use(["ggplot"])


def model(w, x):
    ypred = np.dot(w, x)
    return ypred


def grad_mse(w, xy):

    (x, y) = xy

    # Compute the output
    ypredicted = model(w, x)

    diff = y - ypredicted

    # this gives gradient of both w's
    grad = -np.dot(x, diff)

    return grad


def mse(w, xy):

    (x, y) = xy

    xt = np.transpose(x)

    ypredicted = np.dot(w, x)

    loss = np.sum(
        (y - ypredicted) *
        (y - ypredicted)
    )

    m = 2 * len(y)

    loss = loss / m

    return loss


def gradient_descent(
    xy,
    max_iterations,
    w,
    obj_func,
    mse_func,
    grad_func,
    extra_param=[],
    learning_rate=0.05,
    momentum=0.8
):

    (x, y) = xy

    w_history = w
    f_history = obj_func(w, x)
    cost_history = mse_func(w, xy)

    delta_w = np.zeros(2)

    i = 0

    while i < max_iterations:

        delta_w = -learning_rate * grad_func(w, xy)

        w = w + delta_w

        # store the history of w and f

        w_history = np.vstack((w_history, w))

        ypredicted = obj_func(w, x)

        f_history = np.vstack((f_history, ypredicted))

        cost_history = np.vstack(
            (cost_history, mse_func(w, xy))
        )

        i = i + 1

    return w_history, f_history, cost_history


# ==================================================
# TEST DATA FROM THE VIDEO
# ==================================================

ndim = 2
npoints = 3

w = np.array([0.0, 0.0])

myones = np.ones(npoints)

x = np.arange(0, npoints)

x = np.vstack((myones, x))

y = model(w, x)

y = y + 1

xy = (x, y)

print("xy:")
print(xy)

max_iterations = 100

w_hist, f_hist, c_hist = gradient_descent(
    xy,
    max_iterations,
    w,
    model,
    mse,
    grad_mse,
    learning_rate=0.1,
    momentum=0.8
)

print("\nFinal Weights:")
print(w_hist[-1])

print("\nFinal Cost:")
print(c_hist[-1])

# ==================================================
# PLOT PREDICTION HISTORY
# ==================================================

plt.figure(figsize=(10, 6))

for i in range(len(f_hist)):
    plt.plot(
        x[1],
        f_hist[i],
        "b-",
        alpha=0.5
    )

plt.title("Gradient Descent Parameter Updates")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

# ==================================================
# PLOT COST HISTORY
# ==================================================

plt.figure(figsize=(10, 6))

plt.plot(c_hist)

plt.title("Cost Function History")
plt.xlabel("Iteration")
plt.ylabel("MSE")

plt.show()

