# Module 20: Machine Learning and Advanced Probability

## Overview

This repository contains all coursework, notes, discussions, coding activities, knowledge checks, and the final assignment completed for **Module 20: Machine Learning and Advanced Probability** in the MIT Professional Education Data Engineering Program.

The module introduced foundational machine learning concepts, optimization techniques, Bayesian probability, classification algorithms, and practical implementations using Python and Scikit-learn.

---

## Learning Outcomes

By the end of this module, students should be able to:

- Explain key mathematical concepts used in machine learning.
- Apply Gradient Descent to reduce model error.
- Use Bayes Theorem to calculate conditional probabilities.
- Implement Naive Bayes classification models.
- Implement Gaussian Naive Bayes classification models.
- Build spam detection classifiers using Python.
- Interpret confusion matrices.
- Train and evaluate machine learning models using Scikit-learn.

---

## Topics Covered

### Mathematical Foundations of Machine Learning

- Vectors
- Matrices
- Linear Algebra
- Probability
- Statistics
- Mean Squared Error (MSE)

### Gradient Descent

- Cost Functions
- Gradient Descent
- Learning Rates
- Convergence
- Optimization

### Advanced Probability

- Conditional Probability
- Joint Probability
- Bayes Theorem
- Posterior Probability
- Maximum A Posteriori (MAP)

### Naive Bayes

- Binary Classification
- Multiclass Classification
- Spam Detection
- Feature Independence Assumption

### Gaussian Naive Bayes

- Gaussian Distribution
- Probability Density Functions
- Mean
- Variance
- Standard Deviation
- Continuous Feature Classification

### Classification Evaluation

- Confusion Matrix
- True Positives (TP)
- False Positives (FP)
- False Negatives (FN)
- True Negatives (TN)

### Scikit-Learn

- Model Training
- Model Testing
- train_test_split()
- fit()
- predict()
- accuracy_score()

---

## Repository Structure

```text
Module-20-Machine-Learning-and-Advanced-Probability/
│
├── Videos/
│   ├── Video_20.1_Introduction_to_Machine_Learning.md
│   ├── Video_20.2_Mathematical_Foundations.md
│   ├── Video_20.3_and_20.4_Gradient_Descent.md
│   ├── Video_20.5_Introduction_to_Bayes_Theorem.md
│   ├── Video_20.6_and_20.7_Bayes_Theorem_Exercise.md
│   ├── Video_20.8_Applying_Naive_Bayes_Theorem_to_Detect_Spam_Email.md
│   ├── Video_20.9_and_20.10_Applications_of_Naive_Bayes_Theorem.md
│   ├── Video_20.11_Introduction_to_Gaussian_Naive_Bayes_Theorem.md
│   ├── Mini_Lesson_20.4_Bayes_Theorem.md
│   ├── Mini_Lesson_20.5_Introduction_to_Naive_Bayes_Theorem.md
│   ├── Mini_Lesson_20.6_Detecting_Spam_Emails.md
│   ├── Mini_Lesson_20.7_Introduction_to_the_Confusion_Matrix.md
│   ├── Mini_Lesson_20.8_Introduction_to_Gaussian_Naive_Bayes_Theorem.md
│   └── Mini_Lesson_20.9_Implementing_Machine_Learning_Algorithms_Using_Scikit_Learn.md
│
├── Discussions/
│   ├── Discussion_20.1.md
│   ├── Discussion_20.2_The_Importance_of_Optimizing_Gradient_Descent.md
│   ├── Discussion_20.3_Applications_of_Bayes_Theorem.md
│   └── Discussion_20.4_Use_Cases_for_Naive_Bayes_and_Gaussian_Naive_Bayes.md
│
├── Knowledge_Checks/
│   ├── Knowledge_Check_20.1.md
│   ├── Knowledge_Check_20.2_Gradient_Descent.md
│   └── Knowledge_Check_20.3_Advanced_Probability.md
│
├── Coding_Activities/
│   ├── Coding_Activity_20.1_Optimizing_Gradient_Descent_Using_Learning_Rates.md
│   ├── Coding_Activity_20.1.ipynb
│   ├── Coding_Activity_20.2_Using_Python_for_Spam_Detection.md
│   └── Coding_Activity_20.2.ipynb
│
├── Assignment/
│   ├── Data/
│   │   └── SMSSpamCollection
│   │
│   ├── Notebook/
│   │   └── Module20_assignment_student.ipynb
│   │
│   └── Assignment_20.1_Introduction_to_Machine_Learning_and_Advanced_Probability.md
│
├── Module_20/
│   └── Module_20_Wrap_Up.md
│
└── README.md
```

---

## Coding Activities

### Coding Activity 20.1

**Optimizing Gradient Descent Using Learning Rates**

Concepts:

- Learning Rate Selection
- Optimization
- Local Minima
- Convergence Analysis

Tools Used:

- Python
- NumPy
- Matplotlib

---

### Coding Activity 20.2

**Using Python for Spam Detection**

Concepts:

- Naive Bayes
- Spam Classification
- Confusion Matrix
- Text Processing

Tools Used:

- Python
- Pandas
- NumPy

Dataset:

- SMS Spam Collection Dataset

---

## Final Assignment 20.1

### Part 1: Naive Bayes Classifier

Implemented a simple Naive Bayes classifier using:

- Weather
- Temperature

to predict:

```text
Play Outside
```

Activities:

- Label Encoding
- Feature Creation
- Model Training
- Prediction

---

### Part 2: Multi-Class Classification

Implemented Gaussian Naive Bayes on the Scikit-Learn Wine Dataset.

Activities:

- Dataset Loading
- Training/Test Split
- Classification
- Accuracy Evaluation

Dataset:

```python
from sklearn.datasets import load_wine
```

Classes:

```text
Class_0
Class_1
Class_2
```

---

### Part 3: Spam Detection

Implemented a spam detection classifier using:

```text
SMS Spam Collection Dataset
```

Activities:

- Data Preparation
- CountVectorizer
- Multinomial Naive Bayes
- Model Evaluation

Target Classes:

```text
Ham
Spam
```

---

## Important Formulas

### Mean Squared Error (MSE)

```text
MSE = (1 / 2m) Σ(y - y_hat)^2
```

---

### Gradient Descent

```text
w_new = w_old - (learning_rate * gradient)
```

---

### Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

### Naive Bayes

```text
P(Class | Features)

=

[P(Features | Class) * P(Class)]

/

P(Features)
```

---

### Gaussian Probability Density Function

```text
                 1
f(x) = -------------------------
        σ √(2π)

       * exp(
            -(x - μ)^2
            ----------
             2σ^2
        )
```

---

## Tools and Libraries Used

### Python

Primary programming language.

### NumPy

Used for:

- Numerical operations
- Arrays
- Matrix computations

### Pandas

Used for:

- Data manipulation
- Data exploration
- Data cleaning

### Matplotlib

Used for:

- Gradient Descent visualizations
- Plotting

### Scikit-Learn

Used for:

- Naive Bayes
- Gaussian Naive Bayes
- Model Training
- Data Splitting
- Evaluation Metrics

---

## Datasets Used

### SMS Spam Collection Dataset

Used for:

- Spam Detection
- Text Classification

Target Classes:

```text
Ham
Spam
```

---

### Wine Dataset

Provided by Scikit-Learn.

Target Classes:

```text
Class_0
Class_1
Class_2
```

Features:

```text
Alcohol
Malic Acid
Ash
Alcalinity of Ash
Magnesium
Total Phenols
Flavanoids
Proanthocyanins
Color Intensity
Hue
OD280/OD315
Proline
```

---

## Key Takeaways

- Machine learning models rely heavily on probability and optimization.
- Gradient Descent is fundamental to minimizing prediction error.
- Bayes Theorem provides a framework for updating probabilities based on evidence.
- Naive Bayes offers a fast and effective classification approach.
- Gaussian Naive Bayes extends classification to continuous numerical features.
- Confusion matrices help evaluate classification performance.
- Scikit-Learn simplifies implementation of complex machine learning algorithms.
- Spam detection remains one of the most common real-world applications of Naive Bayes.

---

## Next Module

Upcoming topics build on these foundations by expanding into more advanced machine learning algorithms, model evaluation techniques, and predictive analytics workflows.