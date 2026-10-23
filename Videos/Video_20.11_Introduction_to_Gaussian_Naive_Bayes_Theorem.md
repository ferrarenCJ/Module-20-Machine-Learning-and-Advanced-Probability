# Video 20.11: Introduction to Gaussian Naive Bayes Theorem

**Duration:** 05:22

---

# Overview

In this video, Dr. Williams demonstrates how Gaussian distributions can be used to calculate probability density functions for a population. This concept forms the foundation of the Gaussian Naive Bayes (GNB) classification algorithm.

Unlike standard Naive Bayes, which often relies on frequency counts of categorical variables, Gaussian Naive Bayes is designed for continuous numerical features. It uses the Gaussian probability density function to estimate the likelihood of observing a particular value within a class.

---

# Review of Gaussian Naive Bayes

Gaussian Naive Bayes is based on Bayes Theorem:

```text
P(Class | Features)

=

[P(Features | Class) * P(Class)]

/

P(Features)
```

The key difference is that:

```text
P(Features | Class)
```

is estimated using a Gaussian (Normal) Distribution.

---

# Probability Density Function (PDF)

A Probability Density Function (PDF) describes the relative likelihood of a continuous value occurring within a distribution.

Unlike discrete probabilities:

```text
P(X = x)
```

the PDF provides the density of observations around a value.

The Gaussian PDF allows us to determine how likely it is that a particular measurement came from a given population.

---

# The Gaussian Distribution

A Gaussian distribution is defined by two parameters:

## Mean (μ)

Represents the center of the distribution.

```text
μ = Average Value
```

---

## Standard Deviation (σ)

Measures how spread out observations are from the mean.

```text
σ = √Variance
```

---

# Gaussian Probability Density Function

The Gaussian PDF is given by:

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

Where:

```text
x  = observation

μ  = mean

σ  = standard deviation
```

This function computes the probability density associated with a particular value.

---

# Interpreting the Distribution

The Gaussian distribution forms a bell-shaped curve.

Observations near the mean:

```text
Higher Probability Density
```

Observations farther from the mean:

```text
Lower Probability Density
```

Therefore:

```text
Values near the center
are more likely.
```

---

# Example: Height Distribution

Suppose the male height distribution has:

```text
Mean = 5.85

Variance = 0.035
```

The standard deviation becomes:

```text
σ = √0.035

≈ 0.187
```

A height near:

```text
5.85
```

will have a high probability density.

A height much farther away from:

```text
5.85
```

will have a lower probability density.

---

# Using the PDF in Classification

Suppose we observe:

```text
Height = 5.8
```

The Gaussian PDF is evaluated using:

```text
Male Height Distribution
```

and separately using:

```text
Female Height Distribution
```

This produces:

```text
P(Height | Male)
```

and

```text
P(Height | Female)
```

These values are used as likelihoods in Bayes Theorem.

---

# Combining Multiple Features

Gaussian Naive Bayes often works with several numerical features.

Example:

```text
Height
Weight
Foot Size
```

The model calculates:

```text
P(Height | Class)
```

```text
P(Weight | Class)
```

```text
P(Foot Size | Class)
```

and multiplies them together.

For a male classification:

```text
P(Male)

*

P(Height | Male)

*

P(Weight | Male)

*

P(Foot Size | Male)
```

The same process is repeated for the female class.

---

# Classification Decision

After calculating the posterior probabilities:

```text
P(Male | Features)
```

and

```text
P(Female | Features)
```

the classifier chooses the larger probability.

Example:

```text
If

P(Male | Features)

>

P(Female | Features)

Then:

Classify as Male
```

---

# Why Probability Density Is Important

The probability density function allows continuous numerical data to be incorporated into Bayes Theorem.

Examples include:

- Height
- Weight
- Income
- Temperature
- Age
- Exam Scores

Without the PDF, Naive Bayes would be limited primarily to categorical variables.

---

# Advantages of Gaussian Naive Bayes

## Handles Continuous Data

Works naturally with numerical measurements.

---

## Computationally Efficient

Calculations can be performed quickly even on large datasets.

---

## Simple Implementation

Requires only:

- Mean
- Variance
- Standard Deviation

for each feature and class.

---

## Effective Classification

Often performs surprisingly well despite its simplifying assumptions.

---

# Common Applications

## Medical Diagnosis

Classifying patients using laboratory measurements.

---

## Customer Analytics

Segmenting customers based on numerical attributes.

---

## Credit Risk Analysis

Evaluating borrower characteristics.

---

## Pattern Recognition

Classifying objects using measured features.

---

## Predictive Analytics

Making decisions from continuous data values.

---

# Relationship to Bayes Theorem

Bayes Theorem supplies the framework:

```text
P(Class | Features)
```

while the Gaussian Distribution supplies:

```text
P(Features | Class)
```

Together they allow continuous measurements to be used for classification.

---

# Key Takeaways

- Gaussian Naive Bayes is designed for continuous numerical data.
- The Gaussian distribution is characterized by a mean and standard deviation.
- The Gaussian probability density function estimates likelihoods for continuous features.
- Values closer to the mean generally have higher probability density.
- Multiple feature probabilities are combined using Bayes Theorem.
- The class with the highest posterior probability is selected.
- Gaussian Naive Bayes is widely used for classification and predictive analytics.

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

## Gaussian Probability Density Function

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