# Mini-Lesson 20.2: Mathematics Fundamentals

---

## Why Learn Mathematics for Machine Learning?

Mathematics forms the foundation of Machine Learning (ML). Understanding core mathematical concepts helps explain how machine learning algorithms learn from data, identify patterns, optimize predictions, and make decisions.

Important mathematical topics used throughout ML include:

- Cartesian Planes
- Equations of Lines
- Arrays and Matrices
- Vector Operations
- Dot Products
- Probability
- Derivatives
- Chain Rule
- Logarithms

A strong understanding of these concepts is essential for understanding Gradient Descent, Linear Regression, Neural Networks, and many other machine learning algorithms.

---

# The Cartesian Plane

A Cartesian Plane consists of two perpendicular axes:

- **X-Axis** (Horizontal)
- **Y-Axis** (Vertical)

Any point on the plane can be represented using coordinates:

```text
(x, y)
```

Where:

- x = horizontal position
- y = vertical position

The point:

```text
(0,0)
```

is called the **Origin**.

---

## Quadrants

The Cartesian Plane is divided into four quadrants.

### Quadrant I

```text
(+x, +y)
```

Both coordinates are positive.

Example:

```text
(3, 4)
```

---

### Quadrant II

```text
(-x, +y)
```

Example:

```text
(-3, 4)
```

---

### Quadrant III

```text
(-x, -y)
```

Example:

```text
(-3, -4)
```

---

### Quadrant IV

```text
(+x, -y)
```

Example:

```text
(3, -4)
```

---

# Equation of a Line

A line can be represented using the **Slope-Intercept Form**:

```text
y = mx + b
```

Where:

- m = slope
- b = y-intercept

---

## Slope

The slope determines:

- Direction
- Steepness

Examples:

```text
m > 0
```

Positive slope

```text
m < 0
```

Negative slope

```text
m = 0
```

Horizontal line

---

## Y-Intercept

The y-intercept is where the line crosses the y-axis.

For example:

```text
y = x + 2
```

Crosses the y-axis at:

```text
(0, 2)
```

---

# Arrays and Matrices

Machine Learning relies heavily on arrays and matrices for storing and manipulating data.

---

## Scalar

A scalar contains a single value.

Example:

```text
2
```

Dimension:

```text
1 x 1
```

---

## Vector

A vector contains multiple values organized in a single row or column.

### Row Vector

```text
[1 2 3]
```

Dimension:

```text
1 x 3
```

---

### Column Vector

```text
[1]
[2]
[3]
```

Dimension:

```text
3 x 1
```

---

## Matrix

A matrix contains multiple rows and columns.

Example:

```text
[1 2]
[3 4]
```

Dimensions:

```text
2 x 2
```

Two rows and two columns.

---

# Matrix Operations

## Matrix Addition

Matrices can only be added when they have the same dimensions.

Example:

```text
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]
```

Result:

```text
A + B = [6  8]
        [10 12]
```

---

## Scalar Multiplication

Multiply every element by the scalar value.

Example:

```text
2 ×

[1 2]
[3 4]
```

Result:

```text
[2 4]
[6 8]
```

---

## Matrix Multiplication

Matrix multiplication is only valid when:

```text
Columns in Matrix A
=
Rows in Matrix B
```

Example:

```text
(2 x 3) × (3 x 4)
```

Produces:

```text
(2 x 4)
```

---

# Dot Product

The Dot Product multiplies two vectors and returns a scalar value.

Given:

```text
A = [1 2 3]

B = [4 5 6]
```

Calculation:

```text
(1 × 4)
+
(2 × 5)
+
(3 × 6)
```

Result:

```text
4 + 10 + 18 = 32
```

Therefore:

```text
A · B = 32
```

---

## Why the Dot Product Matters

The Dot Product is heavily used in:

- Linear Regression
- Neural Networks
- Recommendation Systems
- Similarity Calculations
- Machine Learning Optimization

---

# Probability Fundamentals

Probability measures the likelihood of an event occurring.

Probability values range from:

```text
0 ≤ P(Event) ≤ 1
```

Where:

```text
0
```

Impossible event

and

```text
1
```

Certain event

---

## Probability Formula

```text
Probability
=
Favorable Outcomes
/
Total Possible Outcomes
```

---

## Example: Rolling a Die

Find the probability of rolling an even number.

Even numbers:

```text
2, 4, 6
```

Favorable outcomes:

```text
3
```

Total outcomes:

```text
6
```

Result:

```text
P(Even) = 3 / 6 = 0.5
```

---

## Impossible Event

Find the probability of rolling a 7 using a six-sided die.

```text
P(7) = 0 / 6 = 0
```

This event cannot occur.

---

# Derivatives

A derivative measures how quickly a function changes.

In geometry, the derivative represents:

```text
Slope of the tangent line
```

at a specific point.

---

## Common Derivatives

### Constant

```text
f(x) = c

f'(x) = 0
```

---

### Power Rule

```text
f(x) = xⁿ

f'(x) = n·xⁿ⁻¹
```

Example:

```text
f(x) = x⁶

f'(x) = 6x⁵
```

---

### Exponential Function

```text
f(x) = eˣ

f'(x) = eˣ
```

---

# Chain Rule

The Chain Rule is used when one function exists inside another function.

General Form:

```text
f(g(x))
```

Derivative:

```text
f'(g(x)) × g'(x)
```

---

## Example

Given:

```text
(x² + 1)³
```

Outer function:

```text
u³
```

Inner function:

```text
u = x² + 1
```

Derivative:

```text
3(x² + 1)²(2x)
```

---

# Logarithms

A logarithm answers:

> What exponent must a base be raised to in order to produce a given number?

---

## Definition

If:

```text
bˣ = y
```

then

```text
logb(y) = x
```

---

## Example

```text
2³ = 8
```

Therefore:

```text
log₂(8) = 3
```

---

# Common Logarithm Properties

## Product Rule

```text
log(ab)
=
log(a)
+
log(b)
```

---

## Quotient Rule

```text
log(a/b)
=
log(a)
-
log(b)
```

---

## Power Rule

```text
log(aⁿ)
=
n log(a)
```

---

# Why Logarithms Matter in ML

Logarithms appear throughout machine learning:

- Information Theory
- Entropy
- Cross-Entropy Loss
- Logistic Regression
- Neural Networks
- Probability Calculations

---

# Key Takeaways

- Mathematics is the foundation of Machine Learning.
- Cartesian planes and line equations are fundamental to understanding regression.
- Arrays, vectors, and matrices are the core structures used in ML computations.
- Dot Products are essential for many machine learning algorithms.
- Probability provides the foundation for predictive models.
- Derivatives measure rates of change and power optimization algorithms.
- The Chain Rule is critical for Gradient Descent and Neural Networks.
- Logarithms are heavily used in probability, information theory, and machine learning loss functions.

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
