# Module 20: Machine Learning and Advanced Probability

## Overview

Module 20 introduced the fundamental concepts of Machine Learning (ML) and Advanced Probability. The module combined mathematical foundations, optimization techniques, probability theory, classification algorithms, and practical machine learning implementations using Python and Scikit-Learn.

Students progressed from understanding how machine learning models learn from data to implementing real-world classification solutions such as spam detection using Naive Bayes and Gaussian Naive Bayes algorithms.

---

## Learning Outcomes

Upon completion of this module, students should be able to:

- Explain key mathematical foundations of machine learning.
- Apply Gradient Descent to optimize machine learning models.
- Calculate conditional probabilities using Bayes Theorem.
- Implement Naive Bayes classifiers.
- Implement Gaussian Naive Bayes classifiers.
- Evaluate classification models using Confusion Matrices.
- Use Scikit-Learn to build and evaluate machine learning models.
- Apply spam detection and classification techniques using Python.

---

## Topics Covered

### Machine Learning Foundations

Topics included:

- Machine Learning Fundamentals
- Supervised Learning
- Classification Problems
- Model Training
- Prediction and Evaluation

---

### Gradient Descent

Concepts studied:

- Cost Functions
- Derivatives
- Gradients
- Learning Rates
- Optimization
- Local Minima
- Convergence

Applications:

- Linear Regression
- Model Optimization

---

### Bayes Theorem

Topics included:

- Conditional Probability
- Joint Probability
- Posterior Probability
- Prior Probability

Formula:

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

Applications:

- Medical Diagnosis
- Fraud Detection
- Spam Classification

---

### Naive Bayes

Topics included:

- Classification Algorithms
- Feature Independence
- Posterior Probability
- Probability Smoothing
- Maximum A Posteriori (MAP)

Applications:

- Spam Detection
- Document Classification
- Sentiment Analysis

---

### Gaussian Naive Bayes

Concepts studied:

- Gaussian Distribution
- Mean
- Variance
- Standard Deviation
- Probability Density Functions

Applications:

- Continuous Numerical Data Classification
- Scientific Data Analysis
- Predictive Modeling

---

### Confusion Matrix

Topics included:

- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

Used to evaluate the performance of classification algorithms.

---

### Scikit-Learn

Students learned how to:

- Install Scikit-Learn
- Split training and testing data
- Train machine learning models
- Generate predictions
- Evaluate model performance

Common workflow:

```python
model = Algorithm()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)
```

---

## Module Components

### Videos

The videos introduced:

- Machine Learning Concepts
- Gradient Descent
- Bayes Theorem
- Naive Bayes
- Gaussian Naive Bayes
- Scikit-Learn

Location:

```text
Videos/
```

---

### Mini Lessons

Mini lessons provided detailed explanations of:

- Bayesian Probability
- Naive Bayes
- Gaussian Naive Bayes
- Confusion Matrices
- Machine Learning Workflows

Location:

```text
Videos/
```

---

### Discussions

Discussion topics included:

- Gradient Descent Optimization
- Bayes Theorem Applications
- Selecting Appropriate Naive Bayes Models
- Machine Learning Resources

Location:

```text
Discussions/
```

---

### Knowledge Checks

Knowledge checks reinforced:

- Machine Learning Terminology
- Probability Concepts
- Bayes Theorem
- Confusion Matrices
- Classification Metrics

Location:

```text
Knowledge_Checks/
```

---

### Coding Activities

#### Coding Activity 20.1

Optimizing Gradient Descent Using Learning Rates

Concepts:

- Learning Rate Tuning
- Optimization
- Error Minimization

---

#### Coding Activity 20.2

Using Python for Spam Detection

Concepts:

- Naive Bayes Classification
- Text Classification
- Confusion Matrices

Location:

```text
Coding_Activities/
```

---

### Final Assignment

#### Assignment 20.1

Implemented:

- Naive Bayes Classifier
- Gaussian Naive Bayes Classifier
- SMS Spam Detection

Topics:

- Label Encoding
- CountVectorizer
- Classification
- Scikit-Learn Implementation

Location:

```text
Assignment/
```

---

### Cheat Sheets

Quick-reference guides covering:

- Machine Learning
- Bayes Theorem
- Gradient Descent
- Classification
- Scikit-Learn Workflows

Location:

```text
Cheat_Sheets/
```

---

### Glossary

Comprehensive collection of:

- Definitions
- Concepts
- Formulas
- Machine Learning Terminology

Location:

```text
Module_20/
```

---

## Important Formulas

### Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

### Gradient Descent

```text
x_new

=

x_old - η∇f(x)
```

---

### Mean

```text
μ = Σx / n
```

---

### Variance

```text
Variance = Σ(x - μ)^2 / n
```

---

### Standard Deviation

```text
σ = √Variance
```

---

### Independent Events

```text
P(A ∩ B)

=

P(A) * P(B)
```

---

## Technologies Used

### Python

Primary programming language.

---

### Jupyter Notebook

Interactive notebook environment.

---

### NumPy

Used for:

- Arrays
- Mathematical Operations
- Numerical Computation

---

### Pandas

Used for:

- Data Loading
- Data Cleaning
- Data Analysis

---

### Scikit-Learn

Used for:

- Naive Bayes
- Gaussian Naive Bayes
- Model Evaluation
- Train/Test Splits

---

## Datasets Used

### Wine Dataset

Provided by Scikit-Learn.

Classification Target:

```text
Class_0
Class_1
Class_2
```

---

### SMS Spam Collection Dataset

Classification Target:

```text
Ham
Spam
```

Used for:

- Text Classification
- Spam Detection

---

## Repository Structure

```text
Module_20/
│
├── README.md
├── Module_20_Glossary.md
├── Module_20_Wrap_Up.md
│
├── Videos/
├── Discussions/
├── Knowledge_Checks/
├── Coding_Activities/
├── Assignment/
└── Cheat_Sheets/
```

---

## Key Takeaways

- Machine learning relies on mathematical and probabilistic foundations.
- Gradient Descent is one of the most important optimization algorithms.
- Bayes Theorem provides a framework for probability-based prediction.
- Naive Bayes is a simple yet powerful classification algorithm.
- Gaussian Naive Bayes extends classification to continuous numerical features.
- Confusion matrices provide deeper insight into classification performance.
- Scikit-Learn simplifies implementation of machine learning workflows.
- Spam detection is a common real-world application of probabilistic classification models.

---

## Module Summary

Module 20 introduced many of the foundational ideas used in machine learning. Through Gradient Descent, Bayes Theorem, Naive Bayes, Gaussian Naive Bayes, Scikit-Learn, and practical classification exercises, students gained both theoretical understanding and hands-on experience implementing machine learning algorithms. These concepts establish a strong foundation for more advanced machine learning, analytics, and data engineering topics in future modules.