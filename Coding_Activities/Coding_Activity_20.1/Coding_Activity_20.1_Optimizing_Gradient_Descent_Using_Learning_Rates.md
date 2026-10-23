# Coding Activity 20.1: Optimizing Gradient Descent Using Learning Rates

## Activity Information

| Item | Details |
|--------|---------|
| Activity | Coding Activity 20.1 |
| Title | Optimizing Gradient Descent Using Learning Rates |
| Points | 20 |
| Type | Required Activity |
| Learning Outcome | Apply Gradient Descent to reduce error |
| Submission | Jupyter Notebook |

---

# Objective

The objective of this activity is to explore how the learning rate affects the performance and efficiency of the Gradient Descent algorithm.

Gradient Descent is an optimization algorithm that iteratively updates model parameters to minimize a loss function. The learning rate determines the size of each update step and directly influences:

- Convergence speed
- Stability
- Overshooting behavior
- Ability to reach the minimum

---

# Background

The Gradient Descent algorithm updates a variable according to the formula:

```text
x_new = x_old - eta * gradient(x)
```

Where:

- eta = learning rate
- gradient(x) = slope of the function at the current point

The goal is to repeatedly move in the direction opposite of the gradient until a minimum is reached.

---

# Question 1

## Complete the Gradient Descent Function

### Original Code

```python
def gradient_descent(
    gradient, start, learn_rate, n_iter=50, tolerance=1e-06
):
    vector = start

    for _ in range(n_iter):

        diff = -learn_rate * gradient(vector)

        # complete the if statement
        if
            break

        vector += diff

    return vector
```

### Solution

```python
import numpy as np

def gradient_descent(
    gradient, start, learn_rate, n_iter=50, tolerance=1e-06
):
    vector = start

    for _ in range(n_iter):

        diff = -learn_rate * gradient(vector)

        if np.abs(diff) <= tolerance:
            break

        vector += diff

    return vector
```

### Explanation

The stopping condition prevents unnecessary iterations once the update step becomes sufficiently small. When the magnitude of the change falls below the tolerance threshold, the algorithm assumes it has reached a local minimum and terminates.

---

# Question 2

## Update the Learning Rate to 0.8

### Code

```python
gradient_descent(
    gradient=lambda v: 2 * v,
    start=0.4,
    learn_rate=0.8
)
```

### Response

When the learning rate is increased to 0.8, the gradient descent algorithm takes very large steps toward the minimum. These large updates cause the algorithm to overshoot the optimal solution and oscillate around the minimum instead of smoothly converging to it. As a result, the optimization process becomes less stable and may fail to efficiently reach the minimum.

---

# Question 3

## Update the Learning Rate to 0.005

### Code

```python
gradient_descent(
    gradient=lambda v: 2 * v,
    start=0.4,
    learn_rate=0.005
)
```

### Response

When the learning rate is reduced to 0.005, the algorithm takes very small steps toward the minimum. This makes the optimization process more stable and reduces the possibility of overshooting the solution. However, convergence becomes much slower and requires many more iterations before reaching the minimum.

---

# Question 4

## Update the Learning Rate to 0.1

For the function:

```text
f(x) = x^4 - 5x^2 - 3x
```

### Code

```python
gradient_descent(
    gradient=lambda v: 4 * v**3 - 10 * v - 3,
    start=0,
    learn_rate=0.1
)
```

### Response

Reducing the learning rate from 0.2 to 0.1 causes the algorithm to make smaller and more controlled parameter updates. Although convergence may require additional iterations, the optimization path becomes smoother and less likely to overshoot the minimum. This improved stability often results in a more reliable convergence process.

---

# Results Summary

## Learning Rate = 0.8

### Advantages

- Faster movement toward the minimum

### Disadvantages

- Overshooting
- Oscillations
- Potential instability

---

## Learning Rate = 0.005

### Advantages

- Stable convergence
- Precise movement toward the minimum

### Disadvantages

- Slow convergence
- Requires many iterations

---

## Learning Rate = 0.1

### Advantages

- Improved stability
- Reliable convergence
- Reduced overshooting

### Disadvantages

- Slightly slower than larger learning rates

---

# Key Takeaways

- The learning rate controls how quickly Gradient Descent moves through the search space.
- Large learning rates can overshoot the minimum and cause instability.
- Small learning rates improve stability but increase training time.
- Choosing an appropriate learning rate is critical for efficient optimization.
- Gradient Descent balances convergence speed and stability through careful learning rate selection.

---

# Concepts Reinforced

- Gradient Descent
- Learning Rate (eta)
- Convergence
- Optimization
- Local Minimum
- Overshooting
- Numerical Stability

---

# Conclusion

This activity demonstrated the importance of selecting an appropriate learning rate when using Gradient Descent. Large learning rates can speed up convergence but increase the risk of overshooting the minimum, while very small learning rates produce stable but slow optimization. A balanced learning rate often provides the most efficient path toward minimizing the loss function.

---

