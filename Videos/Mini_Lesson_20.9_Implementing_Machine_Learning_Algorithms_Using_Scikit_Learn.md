# Mini-Lesson 20.9: Implementing Machine Learning Algorithms Using Scikit-Learn

## Overview

Scikit-learn is one of the most widely used machine learning libraries in Python. It provides tools for:

- Classification
- Regression
- Clustering
- Model Evaluation
- Data Preprocessing
- Model Selection

One of the major advantages of Scikit-learn is its consistent interface. Most machine learning algorithms follow the same workflow:

1. Import the algorithm
2. Prepare the data
3. Split data into training and testing sets
4. Train the model
5. Make predictions
6. Evaluate performance

This standardized approach makes Scikit-learn one of the most valuable tools for machine learning development.

---

# What Is Scikit-Learn?

Scikit-learn is an open-source Python library designed specifically for machine learning.

The library provides implementations for many common algorithms including:

- Linear Regression
- Logistic Regression
- Naive Bayes
- Decision Trees
- Random Forests
- K-Means Clustering
- Support Vector Machines (SVM)

The library also contains utilities for:

- Data splitting
- Model evaluation
- Feature scaling
- Cross-validation

---

# Installing Scikit-Learn

Scikit-learn can be installed using pip.

```bash
pip install scikit-learn
```

---

# Verifying Installation

Open a terminal:

```bash
python
```

Then run:

```python
import sklearn
```

If no errors occur, Scikit-learn has been installed successfully.

Exit Python:

```python
quit()
```

---

# Training vs Testing Sets

One of the most important concepts in machine learning is separating data into:

```text
Training Data
```

and

```text
Testing Data
```

---

## Why Split the Data?

Suppose a dataset contains:

```text
Hours Studied
```

and

```text
Grade Received
```

A machine learning model must learn patterns from historical examples before making predictions.

If the same dataset is used both to train and evaluate the model, performance estimates may be misleading.

Therefore:

### Training Set

Used to teach the model.

### Testing Set

Used to evaluate the model.

---

# Feature Matrix and Target Variable

Scikit-learn typically separates data into:

```text
X
```

and

```text
y
```

Where:

```text
X = Input Features
```

```text
y = Target Variable
```

Example:

```python
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
```

---

# Understanding the Code

## X Definition

```python
X = dataset.iloc[:, :-1].values
```

Selects:

```text
All rows
All columns except the last column
```

These become the predictor variables.

---

## y Definition

```python
y = dataset.iloc[:, 1].values
```

Selects:

```text
Target Variable
```

that the model will learn to predict.

---

# Splitting Data with train_test_split

Scikit-learn provides a built-in function:

```python
from sklearn.model_selection import train_test_split
```

to divide data into training and testing datasets.

Example:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

---

# Understanding the Parameters

## test_size

```python
test_size=0.2
```

Means:

```text
20% Testing Data
80% Training Data
```

---

## random_state

```python
random_state=0
```

Provides reproducible results.

Using the same random state ensures identical dataset splits each time the code is executed.

---

# Machine Learning Workflow in Scikit-Learn

The general workflow can be summarized as:

```text
Prepare Data

↓

Split Data

↓

Create Model

↓

Train Model

↓

Predict Results

↓

Evaluate Model
```

---

# Example: Linear Regression

## Import Library

```python
from sklearn.linear_model import LinearRegression
```

---

## Create Model

```python
r = LinearRegression()
```

This creates a linear regression classifier object.

---

## Train Model

```python
r.fit(
    X_train,
    y_train
)
```

The `.fit()` function learns the relationship between:

```text
X_train
```

and

```text
y_train
```

---

# Model Parameters

After training, the coefficients of the line can be inspected.

## Intercept

```python
print(r.intercept_)
```

Represents:

```text
w0
```

---

## Coefficients

```python
print(r.coef_)
```

Represents:

```text
w1, w2, ...
```

for each feature.

---

# Making Predictions

Once trained, the model can make predictions on unseen data.

```python
y_pred = r.predict(X_test)
```

This generates predicted target values for the testing data.

---

# General Scikit-Learn Pattern

Most Scikit-learn algorithms use the same structure:

## Step 1

Create Model

```python
model = Algorithm()
```

---

## Step 2

Train Model

```python
model.fit(
    X_train,
    y_train
)
```

---

## Step 3

Make Predictions

```python
predictions = model.predict(
    X_test
)
```

---

## Step 4

Evaluate Results

```python
model.score(...)
```

or

```python
confusion_matrix(...)
```

depending on the problem.

---

# Advantages of Scikit-Learn

## Consistent Interface

Most algorithms use the same syntax.

---

## Extensive Algorithm Library

Supports many machine learning methods.

---

## Easy Model Evaluation

Provides tools for:

- Accuracy
- Precision
- Recall
- Confusion Matrices
- Cross-Validation

---

## Large Community Support

One of the most widely adopted machine learning libraries.

---

# Common Algorithms Available

## Regression

- Linear Regression
- Ridge Regression
- Lasso Regression

---

## Classification

- Naive Bayes
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines

---

## Clustering

- K-Means
- Hierarchical Clustering

---

## Dimensionality Reduction

- Principal Component Analysis (PCA)

---

# Key Takeaways

- Scikit-learn is one of the most important machine learning libraries in Python.
- Most machine learning workflows involve splitting data into training and testing sets.
- Features are stored in X, while the target variable is stored in y.
- The train_test_split() function simplifies dataset partitioning.
- Models are trained using the fit() method.
- Predictions are generated using the predict() method.
- Most Scikit-learn algorithms use a consistent and reusable syntax.
- Scikit-learn supports a wide variety of regression, classification, clustering, and evaluation tools.

---

# Common Scikit-Learn Workflow

## Import Model

```python
from sklearn.linear_model import LinearRegression
```

## Create Model

```python
model = LinearRegression()
```

## Train Model

```python
model.fit(
    X_train,
    y_train
)
```

## Make Predictions

```python
predictions = model.predict(
    X_test
)
```

---

# Important Functions

## Split Data

```python
train_test_split()
```

## Train Model

```python
fit()
```

## Predict Values

```python
predict()
```

## Evaluate Model

```python
score()
```