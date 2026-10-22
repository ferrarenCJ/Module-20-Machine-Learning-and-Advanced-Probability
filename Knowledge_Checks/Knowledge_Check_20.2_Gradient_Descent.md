# Self-Study Knowledge Check 20.2: Gradient Descent

## Activity Information

| Item | Details |
|--------|---------|
| Due Date | October 29, 2026 @ 4:29 PM |
| Points | 0 |
| Questions | 4 |
| Time Limit | None |
| Attempts Allowed | Unlimited |
| Type | Self-Study Activity |

---

## Learning Outcome Addressed

### Module Learning Outcome

- Apply Gradient Descent to reduce error.

---

## Overview

This knowledge check evaluates understanding of:

- Gradient Descent
- Linear Regression Weights
- Mean Squared Error (MSE)
- Learning Rate (η)
- Convergence Behavior
- Local and Global Minima

The activity reinforces concepts covered in:

- Mini-Lesson 20.3: Introduction to Gradient Descent
- Video 20.3: Gradient Descent and the Line of Best Fit
- Video 20.4: Visualizing Gradient Descent Using Matplotlib

---

# Question 1

## In NumPy, how are the weights for a linear regression algorithm represented?

### Correct Answer

✅ **As a row vector**

### Explanation

In Dr. Williams' examples, weights are represented as a NumPy row vector:

```python
w = np.array([0, 0])
```

The elements correspond to:

```text
w₀ = intercept
w₁ = slope
```

The prediction function is:

```python
y = np.dot(w, x)
```

which treats the weights as a row vector.

### Key Takeaway

For this course:

```text
Weights = Row Vector
```

---

# Question 2

## How can the loss function be defined for linear regression?

### Correct Answer

✅ **The loss function can be defined using the least of the mean squared errors.**

### Explanation

Linear regression uses the Mean Squared Error (MSE) to measure prediction error.

The objective is:

```text
Minimize MSE
```

Formula:

```text
MSE = 1/(2m) Σ(y - ŷ)²
```

Where:

- y = actual values
- ŷ = predicted values
- m = number of observations

Gradient Descent minimizes this error function to find the optimal model parameters.

### Key Takeaway

```text
Best Fit Line
=
Minimum Mean Squared Error
```

---

# Question 3

## What is the η used in the gradient descent algorithm of linear regression?

### Correct Answer

✅ **Learning Rate**

### Explanation

The learning rate controls the size of each update step during Gradient Descent.

Update equation:

```text
wnew = wold − η∇J(w)
```

Where:

```text
η = learning rate
```

The learning rate determines:

- How quickly the model converges
- Whether the model overshoots the minimum
- The efficiency of optimization

### Key Takeaway

```text
η = Learning Rate
```

---

# Question 4

## In the gradient descent example provided by Dr. Williams, what is important to keep in mind to find the optimal η?

### Select All That Apply

✅ **A smaller η may take forever to reach the local minimum.**

✅ **A larger η may result in overstepping across the local minimum.**

### Explanation

Choosing an appropriate learning rate is critical.

### Small Learning Rate

```text
η too small
```

Results:

- Slow convergence
- Many iterations required
- Longer training times

---

### Large Learning Rate

```text
η too large
```

Results:

- Overshoots the minimum
- May oscillate around the optimum
- Can prevent convergence

---

### Incorrect Choices

❌ A larger η will help you find the local minimum faster.

While larger learning rates can move faster, they may also overshoot and create instability.

❌ A larger η may result in overstepping across the global minimum.

The videos specifically discuss overshooting the **local minimum**.

### Key Takeaway

The optimal learning rate balances:

```text
Speed
and
Stability
```

---

# Summary of Key Concepts

## Linear Regression

Prediction model:

```text
y = w₀ + w₁x
```

---

## Weight Representation

```text
w = [w₀, w₁]
```

Stored as a row vector.

---

## Cost Function

```text
MSE = 1/(2m) Σ(y - ŷ)²
```

Goal:

```text
Minimize MSE
```

---

## Gradient Descent

Update rule:

```text
wnew = wold − η∇J(w)
```

Where:

```text
η = Learning Rate
```

---

## Learning Rate Behavior

### Small η

```text
Slow convergence
```

### Large η

```text
Risk of overshooting
```

### Optimal η

```text
Fast and stable convergence
```

---

# Final Result

**Score: 4 / 4 Questions Correct**

### Topics Mastered

✅ Linear Regression Weights  
✅ Mean Squared Error (MSE)  
✅ Learning Rate (η)  
✅ Gradient Descent Optimization  

---

## Personal Notes

### Important Formulas

#### Linear Regression

```text
y = w₀ + w₁x
```

#### Mean Squared Error

```text
MSE = 1/(2m) Σ(y - ŷ)²
```

#### Gradient Descent

```text
wnew = wold − η∇J(w)
```

### Questions

-

### Learning Rate Observations

-

### Follow-Up Topics

- Stochastic Gradient Descent (SGD)
- Momentum
- Adaptive Learning Rates
- Optimization Algorithms