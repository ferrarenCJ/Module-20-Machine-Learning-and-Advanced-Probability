# Module 20 Cheat Sheet: Machine Learning and Advanced Probability

## Machine Learning Fundamentals

### Machine Learning (ML)

Machine Learning is a branch of computer science that enables systems to learn patterns from data and improve performance without being explicitly programmed.

### Common ML Tasks

| Task | Example |
|--------|---------|
| Classification | Spam vs. Non-Spam |
| Regression | Predict House Price |
| Clustering | Customer Segmentation |
| Recommendation | Product Suggestions |

---

# Gradient Descent

## Purpose

Used to minimize a cost function by iteratively updating model parameters.

### Formula

```text
x_new = x_old - (learning_rate * gradient)
```

Where:

```text
learning_rate = step size
gradient      = slope of the function
```

---

## Learning Rate Effects

### Large Learning Rate

Pros:

- Faster movement

Cons:

- Overshooting
- Instability
- Divergence

### Small Learning Rate

Pros:

- Stable convergence

Cons:

- Slow training
- More iterations

---

# Bayes Theorem

## Formula

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

### Definitions

| Term | Meaning |
|--------|---------|
| P(A|B) | Posterior Probability |
| P(B|A) | Likelihood |
| P(A) | Prior Probability |
| P(B) | Evidence |

---

## Example

```text
P(Disease | Positive Test)

=

[P(Positive Test | Disease)
 * P(Disease)]

/

P(Positive Test)
```

---

# Conditional Probability

## Formula

```text
P(A|B)
```

Meaning:

```text
Probability of A
given B has occurred
```

---

# Joint Probability

## Formula

```text
P(A ∩ B)
```

Meaning:

```text
Probability of
A and B occurring together
```

---

# Naive Bayes

## Definition

A probabilistic classification algorithm based on Bayes Theorem.

### Assumption

```text
Features are independent
```

---

## Formula

```text
P(Class | Features)

=

[P(Features | Class)
 * P(Class)]

/

P(Features)
```

---

## Advantages

- Fast
- Simple
- Low computational cost
- Works well with text data

---

## Common Applications

- Spam Detection
- Sentiment Analysis
- Document Classification
- Medical Diagnosis

---

# Types of Naive Bayes

## Bernoulli Naive Bayes

Used for:

```text
Binary Features
```

Examples:

```text
0 = Word Absent
1 = Word Present
```

---

## Multinomial Naive Bayes

Used for:

```text
Word Counts
```

Examples:

```text
Spam Detection
Text Classification
```

---

## Gaussian Naive Bayes

Used for:

```text
Continuous Features
```

Examples:

```text
Height
Weight
Income
Temperature
```

Assumes:

```text
Normal Distribution
```

---

# Gaussian Distribution

Also called:

```text
Normal Distribution
```

Characteristics:

- Bell-shaped curve
- Symmetric
- Mean at center

---

## Mean

```text
μ = Σx / n
```

---

## Variance

```text
Variance = Σ(x - μ)^2 / n
```

---

## Standard Deviation

```text
σ = √Variance
```

---

# Maximum A Posteriori (MAP)

## Purpose

Used when multiple classes are possible.

### Rule

```text
Choose the class
with the highest
posterior probability.
```

---

# Probability Smoothing

## Purpose

Prevents:

```text
Zero Probabilities
```

Common Method:

```text
Laplace Smoothing
```

Adds small values to unseen events.

---

# Spam Detection Workflow

## Step 1

Collect Emails

---

## Step 2

Convert Text to Features

Examples:

```text
money
free
winner
offer
```

---

## Step 3

Train Naive Bayes Model

---

## Step 4

Predict:

```text
Spam
```

or

```text
Ham
```

---

# Confusion Matrix

## Purpose

Evaluate classification performance.

### Structure

```text
                    Actual

                Positive Negative

Pred Positive      TP       FP

Pred Negative      FN       TN
```

---

## Definitions

### True Positive (TP)

Correct positive prediction.

Example:

```text
Spam predicted as Spam
```

---

### False Positive (FP)

Incorrect positive prediction.

Example:

```text
Ham predicted as Spam
```

---

### False Negative (FN)

Incorrect negative prediction.

Example:

```text
Spam predicted as Ham
```

---

### True Negative (TN)

Correct negative prediction.

Example:

```text
Ham predicted as Ham
```

---

# Scikit-Learn Workflow

## Import Algorithm

```python
from sklearn.naive_bayes import GaussianNB
```

---

## Create Model

```python
model = GaussianNB()
```

---

## Train Model

```python
model.fit(
    X_train,
    y_train
)
```

---

## Predict

```python
predictions = model.predict(
    X_test
)
```

---

## Evaluate

```python
accuracy_score(
    y_test,
    predictions
)
```

---

# Train/Test Split

## Purpose

Separate data for:

- Training
- Testing

---

## Example

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

---

# Text Vectorization

## CountVectorizer

Converts text into numerical features.

### Example

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

train_data = vectorizer.fit_transform(
    X_train
)
```

---

# Common Datasets Used

## SMS Spam Collection

Target:

```text
ham
spam
```

Algorithm:

```text
Multinomial Naive Bayes
```

---

## Wine Dataset

Classes:

```text
Class_0
Class_1
Class_2
```

Algorithm:

```text
Gaussian Naive Bayes
```

---

# Key Terms

| Term | Definition |
|--------|---------|
| Prior Probability | Probability before observing evidence |
| Posterior Probability | Probability after observing evidence |
| Likelihood | Probability of evidence given class |
| Gradient | Direction of steepest increase |
| Learning Rate | Step size in optimization |
| Local Minimum | Lowest point reached by Gradient Descent |
| Classifier | ML algorithm that predicts labels |
| MAP | Maximum A Posteriori |
| IID | Independent and Identically Distributed |
| TP | True Positive |
| FP | False Positive |
| FN | False Negative |
| TN | True Negative |

---

# Must-Know Formulas

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

## Mean

```text
μ = Σx / n
```

---

## Variance

```text
Variance = Σ(x - μ)^2 / n
```

---

## Standard Deviation

```text
σ = √Variance
```

---

## Independent Events

```text
P(A ∩ B)

=

P(A) * P(B)
```

---

# Exam Tips

✅ Large learning rate → fast but unstable

✅ Small learning rate → stable but slow

✅ Naive Bayes → classification problems

✅ Multinomial NB → word counts

✅ Bernoulli NB → binary features

✅ Gaussian NB → continuous numerical features

✅ MAP → choose highest posterior probability

✅ Confusion Matrix → evaluate classifier performance

✅ CountVectorizer → convert text to numbers

✅ Scikit-Learn workflow:

```text
Import → Split → Train → Predict → Evaluate
```