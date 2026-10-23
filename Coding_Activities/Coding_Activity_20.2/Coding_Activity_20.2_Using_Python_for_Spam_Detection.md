# Coding Activity 20.2: Using Python for Spam Detection

## Activity Information

| Item | Details |
|--------|---------|
| Activity | Coding Activity 20.2 |
| Title | Using Python for Spam Detection |
| Points | 20 |
| Type | Required Coding Activity |
| Learning Outcome | Implement spam detection using Python |
| Submission | Jupyter Notebook |

---

# Objective

The purpose of this activity is to build and evaluate a Naive Bayes spam classifier using the SMS Spam Collection dataset.

The activity demonstrates how machine learning can be used to classify text messages as:

```text
ham    (non-spam)
```

or

```text
spam
```

using Bayesian probability and word frequency analysis.

---

# Activity Overview

In this activity, a Naive Bayes classifier is built from scratch.

The workflow includes:

1. Importing the dataset
2. Performing basic exploratory data analysis
3. Shuffling the dataset
4. Splitting data into training, validation, and testing datasets
5. Training a custom Naive Bayes classifier
6. Evaluating classifier performance
7. Comparing two classifier implementations

---

# Part 1: Importing the Dataset and Exploratory Data Analysis

## Question 1

### Original Code

```python
emails = pd.read_csv(
    '',
    sep='\t',
    names=["label", "email"]
)
```

### Solution

```python
emails = pd.read_csv(
    'SMSSpamCollection',
    sep='\t',
    names=["label", "email"]
)
```

### Explanation

Loads the SMS Spam Collection dataset into a Pandas DataFrame.

The dataset contains:

- ham messages
- spam messages

that will be used to train and evaluate the classifier.

---

## Question 2

### Display First 10 Rows

### Solution

```python
emails.head(10)
```

### Explanation

Displays the first 10 rows of the dataset, allowing inspection of:

- Labels
- Message content
- Dataset structure

---

# Exploratory Data Analysis

### Dataset Shape

```python
emails.shape
```

Shows:

```text
(number of rows, number of columns)
```

---

### Column Names

```python
emails.columns
```

Expected:

```text
label
email
```

---

### Summary Statistics

```python
emails.describe()
```

Provides summary information about the dataset.

---

# Part 2: Shuffling and Splitting Messages

## Question 3

### Shuffle Dataset

### Original Code

```python
emails =
```

### Solution

```python
emails = emails.sample(
    frac=1,
    random_state=0
).reset_index(drop=True)
```

### Explanation

Randomly shuffles all messages while preserving reproducibility.

The index is reset to align with the shuffled data.

---

## Question 4

### Split Labels

### Original Code

```python
traininglbls =
vallbls =
testinglbls =
```

### Solution

```python
traininglbls = lbls[:2500]

vallbls = lbls[2500:3500]

testinglbls = lbls[3500:]
```

### Explanation

Creates:

```text
Training Set
2500 observations

Validation Set
1000 observations

Testing Set
Remaining observations
```

---

# Part 3: Building a Naive Bayes Classifier

The notebook provides a custom implementation of:

```python
class NaiveBayesForSpam
```

The class contains:

### train()

Learns:

- Prior probabilities
- Conditional probabilities

from the training dataset.

---

### predict()

Determines whether a message is:

```text
ham
```

or

```text
spam
```

by repeatedly applying Bayes Theorem.

---

### score()

Computes:

- Classification accuracy
- Confusion matrix

for model evaluation.

---

# Part 4: Explaining the Classifier

## train()

The train function builds the probability model.

It computes:

```text
P(ham)
P(spam)
```

and the likelihood of every word occurring within each class.

---

## predict()

The predict function uses Bayes Theorem to calculate posterior probabilities and classify a message as:

```text
ham
```

or

```text
spam
```

---

## score()

The score function evaluates the classifier by:

- Comparing predictions against true labels
- Computing accuracy
- Building a confusion matrix

---

# Part 5: Training the train Classifier

## Question 5

### Create Spam Email Dataset

### Original Code

```python
spamEmails =
```

### Solution

```python
spamEmails = [
    m
    for (m, l) in zip(
        trainingEmail,
        traininglbls
    )
    if 'spam' in l
]
```

### Explanation

Extracts only spam messages from the training data.

---

### Non-Spam Dataset

Provided by notebook:

```python
nonSpamEmails = [
    m
    for (m, l) in zip(
        trainingEmail,
        traininglbls
    )
    if 'ham' in l
]
```

---

### Train Classifier

```python
clf = NaiveBayesForSpam()

clf.train(
    nonSpamEmails,
    spamEmails
)
```

---

# Part 6: Evaluating train Classifier

## Validation Score

```python
score, confusion = clf.score(
    valEmail,
    vallbls
)
```

---

## Print Accuracy

```python
print(
    "The overall performance is:",
    score
)
```

---

## Print Confusion Matrix

```python
print(
    "The confusion matrix is:\n",
    confusion
)
```

---

## Baseline Comparison

```python
print(
    'new_score',
    len(
        [1 for l in vallbls if 'ham' in l]
    ) / float(len(vallbls))
)
```

### Purpose

Compares the classifier against a simple strategy that always predicts:

```text
ham
```

---

# Part 7: Training the train2 Classifier

The notebook introduces a second classifier implementation.

Unlike train(), this version focuses on words that appear much more frequently in spam messages.

---

## Question 6

### Create Updated Classifier

### Original Code

```python
clf =

clf.
```

### Solution

```python
clf = NaiveBayesForSpam()

clf.train2(
    nonSpamEmails,
    spamEmails
)
```

---

## Evaluate Classifier

Correct variable names:

```python
score_2, confusion_2 = clf.score(
    valEmail,
    vallbls
)
```

### Note

The notebook contains a typo:

```python
valEmails
```

The correct variable is:

```python
valEmail
```

---

## Print Results

```python
print(
    "The overall performance is:",
    score_2
)
```

```python
print(
    "The confusion matrix is:\n",
    confusion_2
)
```

---

# Question 7

## How does the performance of the two classifiers compare?

### Response

The train and train2 classifiers produced similar classification results, but the train2 classifier generally focuses on a smaller subset of highly predictive spam words. By filtering out less informative features, train2 may improve efficiency while maintaining comparable classification accuracy. Both classifiers successfully distinguish between spam and non-spam messages using Naive Bayes probability calculations.

---

# Question 8

## What do the train and train2 classifiers do, and what is the difference between them?

### Response

The train classifier uses all words found in the training dataset to calculate prior and conditional probabilities. The train2 classifier introduces an additional filtering step and keeps only words that are significantly more common in spam messages. As a result, train2 reduces the size of the vocabulary and focuses on highly informative spam indicators, making the classifier more specialized while still relying on the same Naive Bayes principles.

---

# Understanding the Confusion Matrix

The confusion matrix evaluates classification performance.

```text
                    Actual

                Ham     Spam

Pred Ham         TP      FN

Pred Spam        FP      TP
```

The matrix helps identify:

- Correct classifications
- False positives
- False negatives

---

# Key Takeaways

- Naive Bayes is an effective algorithm for spam detection.
- Word frequencies can be used to classify SMS messages.
- Training, validation, and testing datasets are important for evaluating model quality.
- Confusion matrices provide deeper insight than accuracy alone.
- The train and train2 classifiers use the same Bayesian principles but differ in feature selection.
- Spam filtering is one of the most common real-world applications of Naive Bayes classification.

---

# References

- SMS Spam Collection Dataset
- UC Irvine Machine Learning Repository
- Scikit-Learn Naive Bayes Documentation
- Pandas Documentation