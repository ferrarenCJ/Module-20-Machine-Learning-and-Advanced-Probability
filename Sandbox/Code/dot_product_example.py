import numpy as np

# Weight vector
w = np.array([1, 2])

# Number of points
npoints = 5

# Create a vector of ones
myones = np.ones(npoints)

# Create values from 0 to 4
x = np.arange(0, npoints)

# Stack the vectors vertically
x = np.vstack((myones, x))

# Compute the dot product
y = np.dot(w, x)

# Display results
print(f'x = {x}')
print(f'y = {y}')