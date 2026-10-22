# Mini-Lesson 20.1: Introduction to Machine Learning

---

## Overview

Machine Learning (ML) is a subset of Artificial Intelligence (AI) that enables computers to learn patterns from data and make decisions without being explicitly programmed.

By leveraging statistical methods and algorithms, ML models can:

- Discover patterns in data
- Generate insights
- Make predictions
- Improve decision making

Machine Learning has become a foundational technology across industries including healthcare, finance, marketing, retail, and transportation.

---

## Core Concepts in Machine Learning

Machine Learning can be categorized into three primary learning approaches.

### 1. Supervised Learning

Supervised learning uses labeled data where each input has a known output.

#### Characteristics

- Learns from historical examples
- Uses input-output pairs
- Makes predictions on new data

#### Example

Email spam detection where emails are labeled as:

- Spam
- Not Spam

---

### 2. Unsupervised Learning

Unsupervised learning works with unlabeled data to discover hidden structures and patterns.

#### Characteristics

- No predefined answers
- Finds relationships in data
- Identifies clusters and trends

#### Example

Customer segmentation where customers are grouped according to:

- Purchase behavior
- Spending habits
- Product preferences

---

### 3. Reinforcement Learning

Reinforcement learning learns by interacting with an environment and receiving rewards or penalties.

#### Characteristics

- Trial-and-error learning
- Rewards desired behavior
- Penalizes incorrect behavior

#### Example

Training an AI system to play chess by learning from wins and losses.

---

## Common Machine Learning Algorithms

Machine Learning models use different algorithms depending on the problem being solved.

### Linear Regression

Linear Regression predicts continuous numerical values using linear relationships between variables.

#### Example

Predicting house prices based on:

- Square footage
- Number of bedrooms
- Location

---

### Logistic Regression

Logistic Regression is used for classification problems where the result belongs to a specific category.

#### Example

Predicting whether a customer will:

- Buy a product
- Not buy a product

---

### Decision Trees

Decision Trees split data into branches to support decision making.

#### Example

Diagnosing diseases using symptoms and medical observations.

---

### Naïve Bayes

Naïve Bayes is a probabilistic classification algorithm based on Bayes' Theorem.

#### Example

Classifying emails as:

- Spam
- Not Spam

---

### K-Means Clustering

K-Means groups similar observations into clusters.

#### Example

Grouping customers based on purchasing behavior.

---

## Model Evaluation

After building a model, its performance must be evaluated.

### Accuracy

Measures the percentage of correct predictions.

#### Formula

```text
Accuracy = Correct Predictions / Total Predictions
```

---

### Precision

Measures how many predicted positive cases are actually positive.

#### Example

Of all emails predicted as spam, how many were truly spam?

---

### Recall

Measures how many actual positive cases were correctly identified.

#### Example

Of all spam emails received, how many were correctly detected?

---

### F1 Score

The harmonic mean of Precision and Recall.

Used when balancing false positives and false negatives is important.

---

### Confusion Matrix

A table used to compare:

- Actual classifications
- Predicted classifications

It helps identify:

- True Positives
- True Negatives
- False Positives
- False Negatives

---

## Optimization and Gradient Descent

Machine Learning models require optimization to improve prediction accuracy.

### Gradient Descent

Gradient Descent is an optimization algorithm that:

1. Calculates prediction error
2. Adjusts model parameters
3. Repeats the process until error is minimized

Gradient Descent is commonly used in:

- Linear Regression
- Logistic Regression
- Neural Networks
- Deep Learning Models

---

## Overfitting and Underfitting

One of the major challenges in machine learning is ensuring that models generalize well to new data.

### Overfitting

Occurs when a model memorizes training data rather than learning underlying patterns.

#### Characteristics

- Excellent training performance
- Poor test performance
- Sensitive to noise

#### Example

A stock price model that performs well on historical data but fails to predict future trends.

---

### Underfitting

Occurs when a model is too simple to capture meaningful patterns.

#### Characteristics

- Poor training performance
- Poor testing performance
- Misses important relationships

#### Example

A weather model that only considers temperature while ignoring humidity and wind conditions.

---

## Techniques to Reduce Overfitting and Underfitting

### Regularization

Adds penalties for overly complex models.

---

### Cross-Validation

Tests model performance using multiple subsets of the data.

---

### Increasing Training Data

Provides additional examples to improve model learning and generalization.

---

## Real-World Applications of Machine Learning

### Healthcare

- Medical image analysis
- Disease diagnosis
- Patient outcome prediction

---

### Finance

- Fraud detection
- Credit scoring
- Stock market analysis

---

### Retail

- Product recommendations
- Demand forecasting
- Inventory optimization

---

### Transportation

- Route optimization
- Traffic prediction
- Autonomous vehicles

---

## Key Takeaways

- Machine Learning is a branch of Artificial Intelligence focused on learning from data.
- The three primary learning types are Supervised Learning, Unsupervised Learning, and Reinforcement Learning.
- Common algorithms include Linear Regression, Logistic Regression, Decision Trees, Naïve Bayes, and K-Means Clustering.
- Model evaluation uses metrics such as Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.
- Gradient Descent is a critical optimization technique used to minimize model error.
- Overfitting and Underfitting are common modeling challenges.
- Machine Learning is widely used in healthcare, finance, retail, and transportation.

---

## Personal Notes

### New Concepts

-

### Key Examples

-

### Questions

-

### Real-World Applications

-

### Follow-Up Topics

-