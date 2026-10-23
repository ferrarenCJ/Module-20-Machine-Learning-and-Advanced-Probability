# Final Assignment 20.1: Implementing Naive Bayes and Gaussian Naive Bayes Classifiers

## Activity Information

| Item | Details |
|--------|---------|
| Assignment | Final Assignment 20.1 |
| Module | Module 20: Machine Learning and Advanced Probability |
| Points | 100 |
| Type | Required Final Assignment |
| Learning Outcomes | Spam Detection, Naive Bayes, Gaussian Naive Bayes, Scikit-Learn |
| Submission | Jupyter Notebook |

---

# Overview

This assignment focused on implementing Naive Bayes and Gaussian Naive Bayes classifiers using the Python Scikit-Learn library.

The assignment consisted of three parts:

1. Binary classification using a simple weather dataset.
2. Multi-class classification using the Wine dataset.
3. Spam detection using the SMS Spam Collection dataset.

The objective was to gain practical experience applying Bayesian machine learning algorithms, preparing datasets, training classifiers, generating predictions, and evaluating model performance.

---

# Part 1: Naive Bayes Classifier

## Objective

Build a simple classifier that predicts whether an outdoor activity should be played based on:

- Weather
- Temperature

### Dataset

#### Weather

```python
weather = [
    'Sunny','Sunny','Overcast','Rainy',
    'Rainy','Rainy','Overcast','Sunny',
    'Sunny','Rainy','Sunny','Overcast',
    'Overcast','Rainy'
]
```

#### Temperature

```python
temperature = [
    'Hot','Hot','Hot','Mild',
    'Cool','Cool','Cool','Mild',
    'Cool','Mild','Mild','Mild',
    'Hot','Mild'
]
```

#### Target Variable

```python
play = [
    'No','No','Yes','Yes',
    'Yes','No','Yes','No',
    'Yes','Yes','Yes','Yes',
    'Yes','No'
]
```

---

## Question 1

### Encode Weather Labels

```python
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

weather_encoded = le.fit_transform(weather)
```

---

## Question 2

### Encode Temperature and Play Labels

```python
temp_encoded = le.fit_transform(temperature)

play_encoded = le.fit_transform(play)
```

---

## Question 3

### Create Feature Array

```python
import numpy as np

features = np.array([
    weather_encoded,
    temp_encoded
])
```

---

## Build Classifier

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(
    features.reshape(14, 2),
    play_encoded
)
```

---

## Prediction 1

### Weather = Overcast

### Temperature = Mild

```python
predicted = model.predict([[0,2]])
```

### Question 4 Response

The predicted value represents the model's estimate of whether an outdoor activity should be played when the weather is overcast and the temperature is mild. The classifier uses probabilities learned from the training data and predicts the outcome that has the highest probability given those conditions.

---

## Prediction 2

### Weather = Rainy

### Temperature = Hot

```python
predicted = model.predict([[1,1]])
```

### Question 5 Response

The predicted value represents whether the model predicts that an outdoor activity should be played when the weather is rainy and the temperature is hot. The prediction is based on the conditional probabilities learned by the Naive Bayes classifier from the available observations.

---

# Part 2: Multi-Class Classification Using the Wine Dataset

## Objective

Train a Gaussian Naive Bayes classifier capable of predicting one of three wine classes.

---

## Load Dataset

```python
from sklearn import datasets

wine = datasets.load_wine()
```

---

## Features

```python
print(wine.feature_names)
```

The dataset contains 13 numerical features including:

- Alcohol
- Malic Acid
- Ash
- Magnesium
- Flavanoids
- Color Intensity
- Hue
- Proline

---

## Question 6

### Print Labels

```python
print("Labels:", wine.target_names)
```

Output:

```text
class_0
class_1
class_2
```

---

## Question 7

### Training/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    wine.data,
    wine.target,
    test_size=0.3,
    random_state=109
)
```

---

## Question 8

### Create and Train Classifier

```python
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

gnb.fit(
    X_train,
    y_train
)

y_pred = gnb.predict(X_test)
```

---

## Question 9

### Compute Accuracy

```python
from sklearn import metrics

print(
    "Accuracy:",
    metrics.accuracy_score(
        y_test,
        y_pred
    )
)
```

---

## Results

The Gaussian Naive Bayes classifier successfully predicted the wine classifications and produced a classification accuracy score based on the testing dataset.

---

# Part 3: SMS Spam Detection

## Objective

Classify SMS messages as:

```text
Ham (Normal Message)
```

or

```text
Spam
```

using the SMS Spam Collection Dataset.

---

## Load Dataset

```python
import pandas as pd

sms_spam = pd.read_csv(
    'SMSSpamCollection',
    sep='\t',
    header=None,
    names=['label', 'text']
)
```

---

## Question 10

### View Dataset Shape

```python
sms_spam.shape
```

### View First Five Records

```python
sms_spam.head()
```

---

## Question 11

### Examine Class Distribution

```python
sms_spam['label'].value_counts(
    normalize=True
)
```

Result:

```text
Approximately 87% Ham
Approximately 13% Spam
```

---

## Question 12

### Encode Labels

```python
sms_spam['label'] = (
    sms_spam['label']
    .replace({
        'ham': 0,
        'spam': 1
    })
    .astype(int)
)
```

---

## Question 13

### Training/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    sms_spam['text'],
    sms_spam['label'],
    random_state=1
)
```

---

## Feature Vectorization

```python
from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer()

train_data = count_vector.fit_transform(X_train)

test_data = count_vector.transform(X_test)
```

---

## Question 14

### Train Multinomial Naive Bayes Classifier

```python
from sklearn.naive_bayes import MultinomialNB

naive_bayes = MultinomialNB()

naive_bayes.fit(
    train_data,
    y_train
)
```

---

## Generate Predictions

```python
predictions = naive_bayes.predict(
    test_data
)
```

---

## Question 15

### Compute Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy_score = accuracy_score(
    y_test,
    predictions
)
```

```python
print(accuracy_score)
```

---

# Technologies Used

## Python

Primary programming language.

---

## NumPy

Used for numerical arrays and mathematical operations.

---

## Pandas

Used for loading, exploring, and transforming datasets.

---

## Scikit-Learn

Used for:

- Label Encoding
- Training/Test Splits
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Accuracy Evaluation
- Feature Vectorization

---

# Algorithms Used

## Gaussian Naive Bayes

Applied to:

- Weather Dataset
- Wine Dataset

Best suited for:

```text
Continuous Numerical Features
```

---

## Multinomial Naive Bayes

Applied to:

- SMS Spam Collection Dataset

Best suited for:

```text
Word Counts
Text Classification
Document Classification
```

---

# Key Concepts Reinforced

- Bayes Theorem
- Conditional Probability
- Posterior Probability
- Maximum A Posteriori (MAP)
- Naive Bayes Classification
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Label Encoding
- Feature Engineering
- Text Vectorization
- Training/Test Splits
- Accuracy Measurement

---

# Key Takeaways

- Naive Bayes provides an efficient probabilistic approach to classification.
- Gaussian Naive Bayes works well with continuous numerical variables.
- Multinomial Naive Bayes is highly effective for text classification problems.
- CountVectorizer converts text data into numerical features suitable for machine learning.
- Scikit-Learn simplifies the implementation of machine learning algorithms.
- Bayesian methods can be applied to binary classification, multiclass classification, and spam detection problems.
- Proper data preparation is essential for building reliable machine learning models.

---

# Conclusion

This assignment demonstrated the implementation of both Gaussian Naive Bayes and Multinomial Naive Bayes classifiers using Python and Scikit-Learn. The exercises progressed from a simple binary classification problem to a multiclass classification task and finally a real-world spam detection application. These activities reinforced core machine learning concepts including probability-based classification, data preprocessing, feature extraction, model evaluation, and practical use of the Scikit-Learn machine learning framework.
