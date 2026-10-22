import matplotlib.pyplot as plt
import numpy as np

# Number of points
npoints = 10

# Create feature vector
x = np.arange(0, npoints)

# Bias term (intercept)
myones = np.ones(npoints)

# Design matrix
x = np.vstack((myones, x))

# Initial weights
w = np.array([0, 0])

# Prediction
y = np.dot(w, x)

# Initial prediction (blue)
plt.plot(x[1], y, 'b.', label='Initial Prediction')

# Shift prediction upward
y = y + 1

# Updated prediction (red)
plt.plot(x[1], y, 'r.', label='Adjusted Prediction')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Visualization')
plt.legend()
plt.grid(True)

plt.show()