# Mini-Lesson 20.5: Introduction to Naive Bayes Theorem

## Overview

Naive Bayes Theorem (NBT) is a classification algorithm based on Bayes Theorem. It is widely used in machine learning because it is simple to implement, computationally efficient, and performs well on large datasets.

Naive Bayes is frequently applied to:

- Spam detection
- Text classification
- Sentiment analysis
- Medical diagnosis
- Recommendation systems

Although it makes simplifying assumptions about the relationships between features, it often produces surprisingly accurate results.

---

# What Is Naive Bayes Theorem?

Naive Bayes Theorem is a probabilistic classification algorithm that uses Bayes Theorem to predict the probability that a record belongs to a particular class.

The algorithm is called "naive" because it assumes that all features are independent of one another.

For example, suppose we want to classify a tomato based on the following characteristics:

- Red
- Round
- Diameter less than three inches

These features may actually be related, but Naive Bayes assumes they are independent when calculating probabilities.

Although this assumption is often unrealistic, Naive Bayes works remarkably well in many real-world classification problems.

---

# Advantages of Naive Bayes

## Easy Implementation

The algorithm is straightforward to understand and implement.

---

## Fast Training

Naive Bayes can be trained efficiently even on large datasets.

---

## Low Computational Cost

Compared to many advanced classification algorithms, Naive Bayes requires relatively little computational power.

---

## Effective for Large Datasets

The algorithm scales well when processing large amounts of data.

---

# Naive Bayes Formula

The Naive Bayes formula is based directly on Bayes Theorem:

```text
P(C|X)

=

[P(X|C) * P(C)]

/

P(X)
```

Where:

```text
P(C|X)
```

Posterior probability of class C given predictor X.

---

```text
P(C)
```

Prior probability of the class.

---

```text
P(X|C)
```

Likelihood.

Probability of observing predictor X given class C.

---

```text
P(X)
```

Prior probability of predictor X.

---

# Terminology

## Posterior Probability

```text
P(C|X)
```

Probability that a record belongs to a class after observing evidence.

---

## Prior Probability of the Class

```text
P(C)
```

Probability of the class before observing evidence.

---

## Likelihood

```text
P(X|C)
```

Probability of the predictor given the class.

---

## Predictor Probability

```text
P(X)
```

Overall probability of observing the predictor.

---

# Example: Football Team Play Prediction

Suppose a football team keeps track of weather conditions and whether they played on a particular day.

The goal is to determine:

```text
What is the probability that the team plays
given that the weather is sunny?
```

---

# Original Dataset

| Day | Weather | Played |
|------|----------|---------|
| Monday | Sunny | No |
| Tuesday | Rainy | Yes |
| Wednesday | Sunny | Yes |
| Thursday | Cloudy | Yes |
| Friday | Sunny | No |
| Saturday | Rainy | No |
| Sunday | Rainy | Yes |
| Monday | Sunny | Yes |
| Tuesday | Rainy | No |
| Wednesday | Cloudy | No |
| Thursday | Sunny | Yes |
| Friday | Sunny | Yes |
| Saturday | Rainy | Yes |
| Sunday | Cloudy | Yes |

---

# Frequency Table

The first step is converting the dataset into a frequency table.

| Weather | Yes | No |
|-----------|-----|----|
| Sunny | 4 | 2 |
| Rainy | 3 | 2 |
| Cloudy | 2 | 1 |
| Total | 9 | 5 |

---

# Goal

Compute:

```text
P(Play = Yes | Sunny)
```

which represents:

```text
Probability that the team plays
given that the weather is sunny.
```

---

# Step 1: Calculate P(Sunny | Yes)

There are:

```text
4 Sunny days
```

when the team played.

There are:

```text
9 Total Yes outcomes
```

Therefore:

```text
P(Sunny | Yes)

=

4 / 9
```

---

# Step 2: Calculate P(Yes)

There are:

```text
9 Yes outcomes
```

out of:

```text
14 Total observations
```

Therefore:

```text
P(Yes)

=

9 / 14
```

---

# Step 3: Calculate P(Sunny)

There are:

```text
6 Sunny days
```

out of:

```text
14 Total observations
```

Therefore:

```text
P(Sunny)

=

6 / 14
```

---

# Step 4: Apply Naive Bayes

Substitute the values into Bayes Theorem:

```text
P(Yes | Sunny)

=

[(4/9) * (9/14)]

/

(6/14)
```

---

# Step 5: Simplify

```text
P(Yes | Sunny)

=

4 / 6
```

```text
P(Yes | Sunny)

=

0.667
```

---

# Final Result

```text
P(Yes | Sunny)

≈ 66.7%
```

There is approximately a:

```text
66% chance
```

that the football team will play given that the weather is sunny.

---

# Why Frequency Tables Matter

In real-world machine learning applications, datasets can contain:

- Millions of records
- Thousands of features
- Terabytes of data

The process of calculating frequency counts is often the most computationally intensive step of implementing Naive Bayes.

Once the frequencies are known, probability calculations become straightforward.

---

# Why Naive Bayes Is Useful

Naive Bayes makes it possible to:

- Classify observations efficiently
- Analyze large datasets
- Estimate probabilities using existing data
- Build predictive models with limited computational resources

---

# Common Applications

## Spam Detection

Determine whether an email is spam.

---

## Sentiment Analysis

Classify text as positive, neutral, or negative.

---

## Medical Diagnosis

Estimate disease probabilities from symptoms.

---

## Fraud Detection

Identify suspicious transactions.

---

## Document Classification

Assign documents to categories based on content.

---

# Key Takeaways

- Naive Bayes is a classification algorithm built on Bayes Theorem.
- The algorithm assumes features are independent.
- Despite the independence assumption, Naive Bayes performs well in many real-world tasks.
- Frequency tables are often used to compute the required probabilities.
- Naive Bayes is computationally efficient and easy to implement.
- The algorithm is frequently used for spam detection, text classification, fraud detection, and medical diagnosis.
- The football example demonstrated a 66.7% probability that the team would play given sunny weather.

---

# Important Formula

## Naive Bayes Theorem

```text
P(C|X)

=

[P(X|C) * P(C)]

/

P(X)
```

Where:

```text
P(C|X) = Posterior Probability
P(C)   = Prior Probability of the Class
P(X|C) = Likelihood
P(X)   = Prior Probability of the Predictor
```