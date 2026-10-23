# Module 20: Glossary

This glossary contains key terms and definitions introduced throughout Module 20: Machine Learning and Advanced Probability.

---

# A

## Array

In mathematics, an array is an arrangement of elements, such as numbers or symbols, organized into rows and columns.

The simplest array is a scalar, which contains only a single value.

---

# B

## Bayes Theorem

Bayes Theorem is used to calculate the probability of an event occurring given that another related event has already occurred.

Formula:

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

# C

## Cartesian Plane

A two-dimensional coordinate system formed by:

- X-Axis (horizontal)
- Y-Axis (vertical)

The point where the axes intersect is called the origin.

The Cartesian plane contains four quadrants.

---

## Chain Rule

A rule used in calculus to calculate the derivative of a composite function.

If:

```text
y = f(g(x))
```

then:

```text
dy/dx

=

f'(g(x)) * g'(x)
```

---

## Classifier

A classifier is the term commonly used in machine learning to represent an algorithm that predicts categories or classes.

Examples:

- Naive Bayes
- Decision Trees
- Random Forests
- Support Vector Machines

---

## Conditional Probability

The probability of an event occurring given that another event has already occurred.

Notation:

```text
P(A|B)
```

---

## Confusion Matrix

A graphical representation used to evaluate the performance of a classification model.

A binary confusion matrix contains:

```text
True Positives (TP)
False Positives (FP)
False Negatives (FN)
True Negatives (TN)
```

Structure:

```text
                    Actual

                Positive Negative

Pred Positive      TP       FP

Pred Negative      FN       TN
```

---

## Coordinates

An ordered pair used to locate a point on the Cartesian plane.

Example:

```text
(x, y)
```

---

# D

## Derivatives

Derivatives measure the rate of change of a function with respect to a variable.

Geometrically, the derivative represents the slope of the tangent line at a point.

Notation:

```text
f'(x)
```

---

## Disjoint Sets

Sets that share no common elements.

Example:

```text
A ∩ B = ∅
```

---

## Dot Product

A method of multiplying two vectors that results in a scalar value.

Also called:

```text
Scalar Product
```

Commonly used in:

- Linear Algebra
- Machine Learning
- Similarity Calculations

---

# E

## Equation of the Line

The slope-intercept form of a line is:

```text
y = mx + b
```

Where:

- m = slope
- b = y-intercept

---

# G

## Gaussian Naive Bayes Theorem

A variation of Naive Bayes that assumes features follow a Gaussian (Normal) Distribution.

Commonly used for continuous numerical features.

Examples:

- Height
- Weight
- Income
- Temperature

---

## Gradient

The gradient is the multi-variable equivalent of a derivative.

It points in the direction of greatest increase of a function.

Notation:

```text
∇f(x)
```

---

## Gradient Descent

An optimization algorithm used to minimize error functions in machine learning.

Formula:

```text
x_new

=

x_old - η∇f(x)
```

Where:

- η = learning rate
- ∇f(x) = gradient

---

# I

## Imputing

A technique used to fill missing values within a dataset.

Common strategies:

- Mean Imputation
- Median Imputation
- Mode Imputation

---

## Independent and Identically Distributed (IID)

A collection of random variables that:

- Have the same probability distribution
- Are mutually independent

Many machine learning algorithms assume IID data.

---

## Intersection

The set of elements shared by two or more sets.

Notation:

```text
A ∩ B
```

---

# L

## Learning Rate

A parameter used in Gradient Descent that controls the size of each optimization step.

Notation:

```text
η
```

A large learning rate may overshoot the minimum.

A small learning rate may slow convergence.

---

## Line of Best Fit

A line that best represents the relationship between variables in a dataset.

Commonly used in:

- Linear Regression
- Trend Analysis

---

## Local Minimum

The point toward which Gradient Descent attempts to move while minimizing a cost function.

Represents a low point within a region of the function.

---

## Logarithms

A logarithm is the exponent to which a base must be raised to obtain a value.

Example:

```text
2^3 = 8

log₂(8) = 3
```

---

# M

## Machine Learning

A branch of computer science focused on algorithms that improve their performance using data and experience without being explicitly programmed.

Examples:

- Classification
- Regression
- Clustering

---

## Matrix

A two-dimensional array consisting of rows and columns.

General form:

```text
m × n
```

Where:

- m = rows
- n = columns

---

## Maximum A Posteriori (MAP)

A method used to select the class with the highest posterior probability.

Decision Rule:

```text
Choose

argmax P(Class|Data)
```

---

## Multiplication of Independent Events Theorem

For independent events:

```text
P(A ∩ B)

=

P(A) * P(B)
```

---

# N

## Naive Bayes Theorem

A probabilistic classification algorithm based on Bayes Theorem.

The algorithm assumes:

```text
Feature Independence
```

Formula:

```text
P(Class|Features)

=

[P(Features|Class) * P(Class)]

/

P(Features)
```

Common applications:

- Spam Detection
- Sentiment Analysis
- Document Classification

---

# O

## Origin

The point where the X-axis and Y-axis intersect.

Coordinates:

```text
(0,0)
```

---

# P

## Posterior Probability

The updated probability of an event after considering new information.

Notation:

```text
P(A|B)
```

---

## Prior Probability

The probability of an event before observing new information.

Notation:

```text
P(A)
```

---

## Probability Smoothing

A technique used to avoid zero probabilities when events do not appear in the training data.

Common method:

```text
Laplace Smoothing
```

---

## Property of Distribution

A set-theory property that distributes intersections or unions across sets.

Example:

```text
A ∩ (B ∪ C)

=

(A ∩ B) ∪ (A ∩ C)
```

---

# S

## Scalar

An array containing only a single value.

Example:

```text
5
```

---

## Scikit-Learn

An open-source Python library that provides machine learning algorithms and utilities.

Examples:

- Linear Regression
- Naive Bayes
- Decision Trees
- Random Forests

Installation:

```bash
pip install scikit-learn
```

---

## Slope-Intercept Form

One form of the equation of a line.

Formula:

```text
y = mx + b
```

---

## Spam Detection

The process of classifying messages as:

```text
Spam
```

or

```text
Non-Spam (Ham)
```

A common application of Naive Bayes classification.

---

## Stochastic Gradient Descent (SGD)

A variation of Gradient Descent that updates parameters using only a subset of the training data.

Advantages:

- Faster training
- Lower computational cost

---

# T

## Testing Set

A dataset used to evaluate model performance after training.

Not used during training.

---

## Training Set

A dataset used to train a machine learning model.

Contains examples used for learning patterns.

---

# V

## Vector

A one-dimensional array containing multiple values.

Examples:

### Row Vector

```text
[1 2 3]
```

### Column Vector

```text
[1]
[2]
[3]
```

Vectors are fundamental building blocks of:

- Linear Algebra
- Machine Learning
- Data Science

---

# Key Formulas

## Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

## Gradient Descent

```text
x_new

=

x_old - η∇f(x)
```

---

## Independent Events

```text
P(A ∩ B)

=

P(A) * P(B)
```

---

## Equation of a Line

```text
y = mx + b
```

---

## Naive Bayes

```text
P(Class|Features)

=

[P(Features|Class) * P(Class)]

/

P(Features)
```