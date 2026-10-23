# Self-Study Knowledge Check 20.3: Advanced Probability

## Activity Information

| Item | Details |
|--------|---------|
| Due Date | October 29, 2026 @ 4:29 PM |
| Questions | 11 |
| Points | 0 |
| Time Limit | None |
| Attempts Allowed | Unlimited |
| Type | Self-Study Activity |

---

# Learning Outcome Addressed

- Identify key concepts and mathematical foundations of Machine Learning.

---

# Overview

This knowledge check covers advanced probability concepts used in Machine Learning, including:

- Conditional Probability
- Joint Probability
- Bayes Theorem
- Naive Bayes Theorem
- Maximum A Posteriori (MAP)
- Gaussian Naive Bayes
- Probability Density Functions
- Classification
- Confusion Matrices

---

# Question 1

## What is conditional probability if you have two events A and B?

### Correct Answer

✅ The probability of B given that A has occurred is called the conditional probability of B given A.

### Formula

```text
P(B | A)
```

### Explanation

Conditional probability measures the likelihood of an event occurring after another event has already occurred.

---

# Question 2

## What is the probability of rainy and sunny weather happening simultaneously?

### Correct Answer

✅ The answer would be the probability of A intersecting the probability of B.

### Formula

```text
P(A ∩ B)
```

### Explanation

This is known as the joint probability of two events occurring simultaneously.

---

# Question 3

## Given that someone is wealthy (W), what is the probability they are healthy (H)?

### Correct Answer

✅

```text
P(H|W)

=

[P(W|H) * P(H)]

/

P(W)
```

### Explanation

This is the direct application of Bayes Theorem.

---

# Question 4

## How can you classify an email as normal or spam?

### Correct Answer

✅ Compute the ratio of the posterior probabilities for each label (normal and spam).

### Explanation

Naive Bayes classification compares posterior probabilities and selects the class with the larger probability.

---

# Question 5

## Which method can calculate the posterior relative probability for an email containing the word "money"?

### Correct Answer

✅ Naive Bayes theorem

### Explanation

Naive Bayes uses conditional probabilities to estimate whether an email is spam or non-spam.

---

# Question 6

## What does MAP stand for in Machine Learning?

### Correct Answer

✅ Maximum a posteriori

### Explanation

MAP estimation selects the class with the highest posterior probability.

```text
Choose class

argmax P(Class | Features)
```

---

# Question 7

## Which Python library can calculate probability density functions?

### Correct Answer

✅ SciPy

### Explanation

SciPy provides statistical distributions and probability density functions used in Gaussian Naive Bayes and other probabilistic models.

Example:

```python
from scipy.stats import norm
```

---

# Question 8

## For which use case can Naive Bayes be applied?

### Correct Answer

✅ Classification

### Explanation

Naive Bayes is fundamentally a classification algorithm.

Examples:

- Spam Detection
- Sentiment Analysis
- Medical Diagnosis
- Document Classification

---

# Question 9

## What is an advantage of Naive Bayes?

### Correct Answer

✅ Low computing cost

### Explanation

Naive Bayes is:

- Fast
- Computationally efficient
- Easy to implement

This makes it suitable for large datasets.

---

# Question 10

## What is a confusion matrix?

### Correct Answer

✅ A confusion matrix is a graphical representation technique that is used to summarize the performance of a classification algorithm.

### Explanation

A confusion matrix helps evaluate classification performance by comparing:

```text
Predicted Values

vs

Actual Values
```

---

# Question 11

## For a binary classification problem, how is a confusion matrix visually represented?

### Correct Answer

✅ For a binary classification problem, the confusion matrix is represented as a table with two rows and two columns that contains combinations of predicted and actual values.

### Structure

```text
                    Actual

                Positive Negative

Pred Positive      TP       FP

Pred Negative      FN       TN
```

Where:

```text
TP = True Positive
FP = False Positive
FN = False Negative
TN = True Negative
```

---

# Important Concepts Reviewed

## Conditional Probability

```text
P(B | A)
```

Probability of B given A.

---

## Joint Probability

```text
P(A ∩ B)
```

Probability that A and B occur simultaneously.

---

## Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

## Naive Bayes

Classification algorithm based on Bayes Theorem.

---

## Maximum A Posteriori (MAP)

```text
Choose the class with the highest
posterior probability.
```

---

## Gaussian Naive Bayes

Uses probability density functions and normal distributions for continuous numerical features.

---

## Confusion Matrix

Used to evaluate classification algorithms through:

- True Positives
- False Positives
- False Negatives
- True Negatives

---

# Key Takeaways

- Conditional probability measures the probability of one event given another.
- Bayes Theorem allows probabilities to be updated using new information.
- Naive Bayes is commonly used for classification problems.
- MAP estimation selects the class with the highest posterior probability.
- SciPy provides tools for probability density computations.
- Naive Bayes offers low computational cost and efficient performance.
- Confusion matrices provide deeper insight into classification performance than accuracy alone.
- Binary confusion matrices are represented as 2×2 tables.

---

# Final Result

**Score: 11 / 11 Questions Correct**

### Topics Mastered

✅ Conditional Probability

✅ Joint Probability

✅ Bayes Theorem

✅ Naive Bayes

✅ Maximum A Posteriori (MAP)

✅ Gaussian Naive Bayes

✅ SciPy Probability Functions

✅ Classification

✅ Confusion Matrices