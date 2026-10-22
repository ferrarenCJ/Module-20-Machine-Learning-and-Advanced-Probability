# Gradient Descent (Videos 20.3 and 20.4)

**Video 20.3: Gradient Descent and the Line of Best Fit**  
**Duration:** 11:16

**Video 20.4: Visualizing Gradient Descent Using Matplotlib**  
**Duration:** 10:09

---

## Overview

These videos build upon the mathematical foundations introduced earlier in the module and demonstrate how Gradient Descent can be used to find the optimal parameters of a predictive model.

The videos focus on:

- Understanding the Line of Best Fit
- Minimizing prediction error
- Mean Squared Error (MSE)
- Gradient calculations
- Learning Rates
- Model convergence
- Visualizing Gradient Descent using Matplotlib

The demonstrations are implemented entirely in Python using NumPy and Matplotlib.

---

# What is Gradient Descent?

Gradient Descent is an optimization algorithm used to minimize a model's error.

The objective is to find the optimal model parameters:

```text
w₀
w₁
```

that minimize the cost function.

For a linear model:

```text
y = w₀ + w₁x
```

Gradient Descent repeatedly updates the model parameters until the prediction error reaches a minimum.

---

# The Line of Best Fit

Suppose a dataset contains observations that approximately follow a linear relationship.

The goal is to find the line:

```text
y = w₀ + w₁x
```

that best represents the data.

The values:

```text
w₀ = Intercept

w₁ = Slope
```

must be adjusted until the difference between actual and predicted values is minimized.

---

# Cost Function

To measure prediction error, a Cost Function is used.

The videos use the Mean Squared Error (MSE).

### Mean Squared Error

```text
MSE = 1/(2m) Σ(y - ŷ)²
```

Where:

```text
y     = Actual Values
ŷ     = Predicted Values
m     = Number of Observations
```

The objective of Gradient Descent is:

```text
Minimize MSE
```

---

# Gradient of the Cost Function

The gradient measures how much each parameter contributes to prediction error.

For the parameter vector:

```text
w = [w₀, w₁]
```

the gradient is:

```text
∇MSE
```

The gradient indicates the direction of greatest increase in error.

To reduce error, Gradient Descent moves in the opposite direction.

---

# Gradient Descent Update Rule

The update equation is:

```text
wnew = wold − α∇MSE
```

Where:

```text
α = Learning Rate
```

The Learning Rate controls how far the algorithm moves during each iteration.

---

# Learning Rate

The Learning Rate is one of the most important hyperparameters in machine learning.

---

## Small Learning Rate

```text
α = 0.001
```

Characteristics:

- Stable updates
- Slow convergence
- Many iterations required

---

## Moderate Learning Rate

```text
α = 0.01
```

Characteristics:

- Faster convergence
- Stable optimization
- Common choice

---

## Larger Learning Rate

```text
α = 0.05
```

Characteristics:

- Faster movement
- Can overshoot the minimum
- Risk of instability

---

# Python Implementation

The videos implement several helper functions.

---

## model()

Used to generate predictions.

```python
y = np.dot(w, x)
```

This represents:

```text
y = w₀ + w₁x
```

---

## mse()

Calculates Mean Squared Error.

Purpose:

```text
Measure prediction error.
```

---

## grad_mse()

Calculates the gradient of the cost function.

Purpose:

```text
Determine how the parameters should change.
```

---

## gradient_descent()

Iteratively updates:

```text
w₀
w₁
```

until a minimum error solution is found.

The function also stores:

```text
Weight History
Prediction History
Cost History
```

which are used for visualization.

---

# Visualizing Gradient Descent

A major focus of the videos is understanding how Gradient Descent behaves visually.

Several visualizations are created using Matplotlib:

### Prediction Updates

Shows how the line of best fit changes during training.

Each iteration generates a new prediction line as:

```text
w₀
w₁
```

are updated.

---

### Cost Function History

Plots:

```text
Cost vs Iteration
```

A successful Gradient Descent implementation should show:

```text
Cost decreasing over time.
```

---

### Contour Plots

The videos visualize the optimization process in parameter space.

The contour plots display:

```text
w₀ (Intercept)
w₁ (Slope)
```

and represent locations where the cost function has equal values.

---

### Weight History

The optimization path is visualized using:

```python
w_hist[:,0]
w_hist[:,1]
```

Each point represents a parameter update.

The resulting path illustrates how Gradient Descent moves toward the minimum cost solution.

---

# Learning Rate Comparison

The videos compare multiple learning rates:

```text
0.001
0.01
0.03
0.05
0.10
```

and demonstrate their impact on convergence.

### Observation 1

Small learning rates require more iterations.

---

### Observation 2

Moderate learning rates generally provide faster convergence.

---

### Observation 3

Large learning rates can overshoot the optimal solution and may cause instability.

---

# Python Libraries Used

### NumPy

Used for:

- Arrays
- Matrices
- Dot Products
- Numerical Calculations

---

### Matplotlib

Used for:

- Line Plots
- Cost History Plots
- Gradient Descent Visualizations
- Contour Plots

To ensure compatibility with the lesson examples:

```bash
pip install --upgrade matplotlib
```

---

# Key Takeaways

- Gradient Descent is an optimization algorithm used to minimize prediction error.
- The Mean Squared Error (MSE) is used as the cost function.
- The gradient identifies how model parameters should be updated.
- The Learning Rate controls the size of parameter updates.
- Smaller learning rates are more stable but converge slowly.
- Larger learning rates converge faster but may overshoot the minimum.
- Weight history and contour plots provide valuable insight into the optimization process.
- NumPy and Matplotlib are essential tools for implementing and visualizing Gradient Descent.

---

# Related Files

### Sandbox

```text
Sandbox/
└── Gradient_Descent/
    ├── gradient_descent.ipynb
    ├── gradient_descent_learning_rate_visualization.ipynb
    ├── gradient_descent_cost_surface.ipynb
    └── README.md
```

These notebooks contain the Python implementations and visualizations demonstrated in Videos 20.3 and 20.4.

---

## Personal Notes

### New Concepts

-

### Questions

-

### Learning Rate Observations

-

### Real-World Applications

-

### Follow-Up Topics

-