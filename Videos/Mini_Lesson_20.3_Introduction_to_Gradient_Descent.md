# Mini-Lesson 20.3: Introduction to Gradient Descent

---

## Overview

Gradient Descent is one of the most important optimization algorithms in Machine Learning (ML).

Its primary purpose is to reduce prediction error by iteratively adjusting model parameters until a minimum error is achieved.

Many machine learning algorithms rely on Gradient Descent, including:

- Linear Regression
- Logistic Regression
- Neural Networks
- Deep Learning Models

In this lesson, Gradient Descent is introduced as an optimization technique that minimizes the error produced by machine learning models.

---

## Why Gradient Descent Matters

Consider a Linear Regression model.

The model makes predictions using a mathematical equation:

```text
y = mx + b
```

However, the predicted values are rarely perfect.

There will usually be some error between:

- Actual values
- Predicted values

Gradient Descent provides a systematic way to reduce these errors and improve the model's accuracy.

---

# Basic Intuition

Imagine standing at the top of a hill and trying to reach the bottom as quickly as possible.

Several paths exist that lead down the hill.

The logical choice is to move in the direction of the steepest downward slope.

This is essentially how Gradient Descent works.

Instead of finding the lowest point of a hill, the algorithm finds the minimum value of an error function.

---

## Relationship to Derivatives

As learned previously:

```text
Derivative = Rate of Change
```

The derivative tells us:

- How quickly a function changes
- Which direction increases most rapidly
- Which direction decreases most rapidly

The derivative always points toward the steepest change of a function.

For a single-variable function:

```text
f(x)
```

the derivative is:

```text
f'(x)
```

---

# The Gradient

For functions with multiple variables, the equivalent of a derivative is called the **Gradient**.

For example:

```text
f(x, y)
```

depends on two variables:

- x
- y

To analyze the function, we calculate:

### Partial Derivative with Respect to x

Treat y as a constant.

```text
∂f/∂x
```

---

### Partial Derivative with Respect to y

Treat x as a constant.

```text
∂f/∂y
```

---

## Gradient Vector

The gradient is a vector containing all partial derivatives:

```text
∇f =
[
∂f/∂x,
∂f/∂y
]
```

The gradient indicates:

- The direction of maximum increase
- The steepest upward path

To move toward a minimum, we move in the opposite direction.

---

# Gradient Descent

Gradient Descent is an optimization algorithm used to minimize a function.

In machine learning, the function being minimized is usually the:

```text
Cost Function
```

or

```text
Error Function
```

The objective is to find parameter values that produce the smallest possible error.

---

## Gradient Descent Equation

The update rule is:

```text
θnew = θold − α∇J(θ)
```

Where:

```text
θ
```

Current parameter values

```text
α
```

Learning Rate

```text
∇J(θ)
```

Gradient of the cost function

---

## How Gradient Descent Works

### Step 1

Initialize model parameters.

---

### Step 2

Calculate prediction error.

---

### Step 3

Compute the gradient.

---

### Step 4

Move parameters in the opposite direction of the gradient.

---

### Step 5

Repeat until the error reaches a minimum.

---

# Cost Function

The Cost Function measures the total prediction error of a model.

Examples include:

### Linear Regression

Mean Squared Error (MSE)

```text
MSE =
Σ(Actual − Predicted)² / n
```

---

### Classification Models

Cross-Entropy Loss

Used in:

- Logistic Regression
- Neural Networks

---

# Local Minimum

A local minimum is the point where the error function reaches its lowest value in a specific area.

Graphically:

```text
          •
        /   \
      /       \
    /           \
  /               \
--------------------
       Minimum
```

The goal of Gradient Descent is to reach this minimum as efficiently as possible.

---

# Learning Rate

One of the most important Gradient Descent parameters is the Learning Rate.

Represented by:

```text
α
```

The learning rate determines how large each step will be.

---

## Learning Rate Too Small

```text
α = very small
```

Results:

- Slow convergence
- More iterations required
- Increased training time

---

## Learning Rate Too Large

```text
α = very large
```

Results:

- Overshoot the minimum
- Miss the optimal solution
- Failure to converge

---

## Appropriate Learning Rate

Results:

- Faster convergence
- Stable optimization
- Improved model performance

---

# Hill-Climbing Analogy

Imagine descending a mountain:

### Small Steps

```text
Safe
Accurate
Slow
```

---

### Large Steps

```text
Fast
Risky
May miss the destination
```

Choosing an appropriate learning rate balances speed and accuracy.

---

# Gradient Descent vs Stochastic Gradient Descent

There are multiple types of Gradient Descent.

---

## Standard Gradient Descent

Uses:

```text
Entire Training Dataset
```

for every iteration.

### Advantages

- More stable updates
- More accurate minimization

### Disadvantages

- Computationally expensive
- Slow for large datasets

---

## Stochastic Gradient Descent (SGD)

Uses:

```text
One Training Sample
```

at each iteration.

### Advantages

- Faster updates
- More scalable
- Reduces training time

### Disadvantages

- Less stable
- More noisy updates
- May not reach the exact minimum

---

## Comparison

| Gradient Descent | Stochastic Gradient Descent |
|------------------|-----------------------------|
| Uses all training samples | Uses one training sample |
| Slower | Faster |
| More stable | More noisy |
| More accurate optimization | Approximate optimization |

---

# Real-World Applications

Gradient Descent is used in:

### Linear Regression

Optimizes slope and intercept parameters.

### Logistic Regression

Optimizes classification boundaries.

### Neural Networks

Adjusts weights during backpropagation.

### Deep Learning

Powers training of modern AI models.

### Computer Vision

Image classification and object detection.

### Natural Language Processing

Text classification and language models.

---

# Key Takeaways

- Gradient Descent is an optimization algorithm used to minimize prediction error.
- The gradient points in the direction of greatest increase.
- Gradient Descent moves in the opposite direction of the gradient.
- The cost function measures model error.
- The local minimum represents the optimal solution.
- The learning rate controls step size during optimization.
- Stochastic Gradient Descent uses a subset of training data and is generally faster than standard Gradient Descent.
- Gradient Descent is foundational to modern Machine Learning and Deep Learning.

---

## Important Formulas

### Gradient

```text
∇f =
[
∂f/∂x,
∂f/∂y
]
```

### Gradient Descent Update Rule

```text
θnew = θold − α∇J(θ)
```

---

## Personal Notes

### New Concepts

-

### Questions

-

### Real-World Applications

-

### Follow-Up Topics

-