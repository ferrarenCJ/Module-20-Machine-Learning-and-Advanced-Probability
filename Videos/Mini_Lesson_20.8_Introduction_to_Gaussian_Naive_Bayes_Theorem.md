# Mini-Lesson 20.8: Introduction to Gaussian Naive Bayes Theorem

## Overview

Gaussian Naive Bayes (GNB) is a classification algorithm based on Naive Bayes that is specifically designed to work with continuous numerical data.

Like all classification algorithms, the goal of Gaussian Naive Bayes is to determine the probability that an observation belongs to a particular class. Unlike standard Naive Bayes, which often uses frequency counts of categorical features, Gaussian Naive Bayes assumes that the features follow a normal (Gaussian) distribution.

Common applications include:

- Medical diagnosis
- Customer segmentation
- Gender classification
- Credit risk analysis
- Predictive analytics

---

# What Is Gaussian Naive Bayes?

Gaussian Naive Bayes extends Bayes Theorem by using the Gaussian (Normal) Distribution to estimate probabilities.

Instead of counting word frequencies or categories, GNB computes probabilities using:

- Mean
- Variance
- Standard Deviation
- Normal Distribution Curves

This allows GNB to classify observations with continuous numerical features.

---

# What Is a Gaussian Distribution?

A Gaussian Distribution, also called a Normal Distribution, is a probability distribution that forms a bell-shaped curve.

Characteristics:

- Symmetrical around the mean
- Mean, median, and mode are equal
- Most observations cluster around the center
- Fewer observations occur farther from the mean

The Gaussian distribution is commonly used to model naturally occurring measurements such as:

- Height
- Weight
- Income
- Temperature
- Test scores

---

# Measurement Dataset Example

| Person | Height | Weight | Foot Size |
|----------|--------|---------|-----------|
| Male | 6.00 | 180 | 12 |
| Male | 5.92 | 190 | 11 |
| Male | 5.58 | 170 | 12 |
| Male | 5.91 | 165 | 10 |
| Female | 5.00 | 100 | 6 |
| Female | 5.50 | 150 | 8 |
| Female | 5.42 | 130 | 7 |
| Female | 5.75 | 150 | 9 |

The objective is to classify a person as:

```text
Male
```

or

```text
Female
```

using:

- Height
- Weight
- Foot Size

---

# Calculating the Mean

The mean of a dataset is calculated as:

```text
Mean = Sum of Values / Number of Values
```

Given n observations:

```text
μ = (x1 + x2 + ... + xn) / n
```

---

# Means for the Dataset

| Person | Height Mean | Weight Mean | Foot Size Mean |
|----------|------------|-------------|---------------|
| Male | 5.85 | 176.25 | 11.25 |
| Female | 5.42 | 132.50 | 7.50 |

These means represent the center of each distribution.

---

# Calculating the Variance

Variance measures how spread out the observations are relative to the mean.

Formula:

```text
Variance = Σ(x - μ)^2 / n
```

Where:

```text
x = observation
μ = mean
n = number of observations
```

A larger variance indicates greater spread.

---

# Variances for the Dataset

| Person | Height Variance | Weight Variance | Foot Size Variance |
|----------|----------------|----------------|-------------------|
| Male | 0.035 | 122.92 | 0.917 |
| Female | 0.097 | 558.33 | 1.667 |

These variances describe how much each feature varies within each class.

---

# Standard Deviation

To plot a Gaussian distribution, the standard deviation is required.

Formula:

```text
Standard Deviation = Square Root of Variance
```

Example:

```text
σ = √Variance
```

For Male Height:

```text
σ = √0.035

≈ 0.187
```

---

# Creating Gaussian Distributions

Once the mean and standard deviation are known, a normal distribution curve can be created for each feature and class.

Examples:

## Height Distribution

Separate distributions are created for:

```text
Male Height
```

and

```text
Female Height
```

using their respective means and variances.

---

## Weight Distribution

Separate distributions are created for:

```text
Male Weight
```

and

```text
Female Weight
```

---

## Foot Size Distribution

Separate distributions are created for:

```text
Male Foot Size
```

and

```text
Female Foot Size
```

---

# Case Study

Suppose an observation contains:

```text
Height = 5.8

Weight = 185

Foot Size = 11
```

The objective is to determine:

```text
Male

or

Female
```

---

# Step 1: Calculate Male Probability

The values:

```text
Height = 5.8
Weight = 185
Foot Size = 11
```

are evaluated using the Male Gaussian distributions.

The resulting probabilities are multiplied together:

```text
P(Height|Male)

×

P(Weight|Male)

×

P(FootSize|Male)
```

and multiplied by the prior probability:

```text
P(Male)
```

---

# Prior Probability

Because the dataset contains:

```text
4 males
4 females
```

the prior probability is:

```text
P(Male) = 0.50

P(Female) = 0.50
```

These probabilities are included in the final calculation.

---

# Step 2: Calculate Female Probability

The same measurements are evaluated using:

```text
Female Height Distribution

Female Weight Distribution

Female Foot Size Distribution
```

The probabilities are multiplied together and weighted by:

```text
P(Female)
```

---

# Step 3: Compare Probabilities

After calculating:

```text
P(Male | Features)
```

and

```text
P(Female | Features)
```

the larger probability determines the classification.

If:

```text
P(Male | Features)

>

P(Female | Features)
```

then the observation is classified as:

```text
Male
```

---

# Why Gaussian Naive Bayes Works

Instead of requiring categorical values such as:

```text
Spam

Not Spam
```

Gaussian Naive Bayes handles continuous numerical features naturally.

Examples:

```text
Height
Weight
Foot Size
Temperature
Age
Income
```

The algorithm converts numerical values into probabilities using the Gaussian distribution.

---

# Advantages of Gaussian Naive Bayes

## Fast Training

Requires relatively little computational power.

---

## Effective for Numerical Data

Handles continuous variables directly.

---

## Easy Implementation

Simple mathematical foundations.

---

## Scalable

Works efficiently on large datasets.

---

# Applications

## Medical Diagnosis

Classifying diseases based on patient measurements.

---

## Credit Risk Analysis

Predicting loan approval outcomes.

---

## Customer Analytics

Classifying customer behavior.

---

## Employee Analytics

Predicting performance categories.

---

## Pattern Recognition

Recognizing object classes from measurements.

---

# Relationship to Bayes Theorem

Bayes Theorem:

```text
P(Class | Features)

=

[P(Features | Class) * P(Class)]

/

P(Features)
```

Gaussian Naive Bayes modifies:

```text
P(Features | Class)
```

by estimating these probabilities using Gaussian distributions.

---

# Key Takeaways

- Gaussian Naive Bayes is a classification algorithm based on Bayes Theorem.
- It is designed for continuous numerical features.
- The algorithm uses Gaussian (Normal) Distributions to estimate probabilities.
- Mean and variance are calculated separately for each feature and class.
- Standard deviation is the square root of variance.
- The class with the highest posterior probability is selected.
- Common applications include medical diagnosis, analytics, and predictive modeling.

---

# Important Formulas

## Bayes Theorem

```text
P(Class | Features)

=

[P(Features | Class) * P(Class)]

/

P(Features)
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

## Gaussian Naive Bayes Decision Rule

```text
Choose the class with the largest posterior probability.
```

---

# Reference

Bognar, M. (2021). *Normal Distribution*. University of Iowa Department of Statistics and Actuarial Science.

https://homepage.divms.uiowa.edu/~mbognar/applets/normal.html