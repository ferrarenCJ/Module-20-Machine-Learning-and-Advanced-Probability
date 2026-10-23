# Final Assignment 20.1: Implementing Naive Bayes and Gaussian Naive Bayes Classifiers

## Overview

This assignment demonstrates the implementation of Naive Bayes and Gaussian Naive Bayes classifiers using Python and the Scikit-Learn library.

The assignment is divided into three parts:

1. Binary classification using a simple weather dataset.
2. Multi-class classification using the Scikit-Learn Wine dataset.
3. Spam detection using the SMS Spam Collection dataset.

The objective is to gain practical experience applying Bayesian machine learning algorithms, preparing datasets, training models, generating predictions, and evaluating classification performance.

---

## Learning Outcomes

Upon completion of this assignment, the following learning outcomes have been achieved:

- Implement spam detection using Python.
- Implement Naive Bayes classifiers using Scikit-Learn.
- Implement Gaussian Naive Bayes classifiers using Scikit-Learn.
- Train and evaluate machine learning classification models.
- Work with binary and multi-class classification problems.
- Apply text preprocessing and feature extraction techniques.

---

# Part 1: Naive Bayes Classifier

## Objective

Build a simple Naive Bayes classifier using weather and temperature data to predict whether an outdoor activity should be played.

### Features

- Weather
- Temperature

### Target Variable

- Play

Possible outputs:

```text
Yes
No
```

---

## Tasks Completed

### Question 1

Encoded the weather labels using:

```python
LabelEncoder()
```

### Question 2

Encoded:

- Temperature
- Play

labels into numerical values.

### Question 3

Created a NumPy feature array using:

```python
weather_encoded
temp_encoded
```

### Question 4

Predicted whether to play when:

```text
Weather = Overcast
Temperature = Mild
```

### Question 5

Predicted whether to play when:

```text
Weather = Rainy
Temperature = Hot
```

---

## Concepts Demonstrated

- Label Encoding
- Feature Engineering
- Gaussian Naive Bayes
- Binary Classification

---

# Part 2: Multi-Class Classification Using the Wine Dataset

## Objective

Apply Gaussian Naive Bayes to a dataset containing three wine classifications.

Dataset Source:

```python
from sklearn.datasets import load_wine
```

---

## Features

The Wine dataset contains 13 numerical features:

- Alcohol
- Malic Acid
- Ash
- Alcalinity of Ash
- Magnesium
- Total Phenols
- Flavanoids
- Nonflavanoid Phenols
- Proanthocyanins
- Color Intensity
- Hue
- OD280/OD315
- Proline

---

## Target Classes

```text
Class_0
Class_1
Class_2
```

---

## Tasks Completed

### Question 6

Displayed:

```python
wine.target_names
```

### Question 7

Created training and testing datasets using:

```python
train_test_split()
```

Parameters:

```python
test_size = 0.3
random_state = 109
```

### Question 8

Implemented:

```python
GaussianNB()
```

Performed:

```python
fit()
predict()
```

### Question 9

Evaluated model performance using:

```python
metrics.accuracy_score()
```

---

## Concepts Demonstrated

- Multi-Class Classification
- Gaussian Naive Bayes
- Training/Test Splits
- Classification Accuracy

---

# Part 3: Spam Detection Using SMS Messages

## Objective

Build a machine learning classifier that predicts whether a text message is:

```text
Ham
```

or

```text
Spam
```

using the SMS Spam Collection dataset.

---

## Dataset

```text
SMSSpamCollection
```

Dataset Size:

```text
5,572 SMS Messages
```

---

## Tasks Completed

### Question 10

Examined the dataset using:

```python
sms_spam.shape
```

and

```python
sms_spam.head()
```

### Question 11

Analyzed class distribution using:

```python
value_counts(normalize=True)
```

### Question 12

Encoded target values:

```text
ham  -> 0
spam -> 1
```

### Question 13

Split the text messages into:

- Training Set
- Testing Set

using:

```python
train_test_split()
```

with:

```python
random_state = 1
```

### Question 14

Vectorized SMS messages using:

```python
CountVectorizer()
```

and trained a:

```python
MultinomialNB()
```

classifier.

### Question 15

Evaluated model accuracy using:

```python
accuracy_score()
```

---

## Concepts Demonstrated

- Text Classification
- Spam Detection
- CountVectorizer
- Multinomial Naive Bayes
- Model Evaluation

---

# Technologies Used

## Python

Primary programming language.

---

## NumPy

Used for:

- Arrays
- Numerical computations

---

## Pandas

Used for:

- Dataset loading
- Data exploration
- Data preprocessing

---

## Scikit-Learn

Used for:

- Label Encoding
- Train/Test Splits
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Accuracy Metrics

---

# Machine Learning Workflow

The following workflow was applied throughout the assignment:

```text
Load Data

↓

Prepare Features

↓

Encode Labels

↓

Split Training/Test Data

↓

Train Model

↓

Generate Predictions

↓

Evaluate Accuracy
```

---

# Key Algorithms Used

## Gaussian Naive Bayes

Used for:

- Weather Dataset
- Wine Dataset

Appropriate when features are continuous numerical values.

---

## Multinomial Naive Bayes

Used for:

- SMS Spam Classification

Appropriate when features represent word counts or frequencies.

---

# Key Takeaways

- Naive Bayes is an efficient probabilistic classification algorithm.
- Gaussian Naive Bayes is well suited for continuous numerical data.
- Multinomial Naive Bayes performs effectively for text classification problems.
- Text data must be vectorized before machine learning algorithms can process it.
- Training and testing datasets are essential for evaluating model performance.
- Scikit-Learn provides a consistent and simple interface for implementing machine learning algorithms.

---

# Files Included

```text
Assignment/
│
├── Data/
│   └── SMSSpamCollection
│
├── Notebook/
│   └── Module20_assignment_student.ipynb
│
├── Assignment_20.1_Introduction_to_Machine_Learning_and_Advanced_Probability.md
│
└── README.md
```

---

# References

- Scikit-Learn Documentation
- UCI SMS Spam Collection Dataset
- MIT Professional Education Data Engineering Program
- Module 20: Machine Learning and Advanced Probability