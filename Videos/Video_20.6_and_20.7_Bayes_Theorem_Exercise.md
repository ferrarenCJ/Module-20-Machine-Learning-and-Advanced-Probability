# Bayes Theorem Exercise (Videos 20.6 and 20.7)

**Video 20.6: Bayes Theorem Exercise**  
**Duration:** 02:19

**Video 20.7: Bayes' Theorem Solution**  
**Duration:** 02:51

---

# Overview

These videos provide a practical application of Bayes Theorem by answering the question:

```text
What percentage of rich people are happy?
```

Video 20.6 introduces the problem and defines the known probabilities, while Video 20.7 demonstrates how to apply Bayes Theorem to calculate the desired conditional probability.

The exercise reinforces the concepts introduced in Mini-Lesson 20.4 and demonstrates how Bayes Theorem can be used to update beliefs based on observed information.

---

# Problem Statement

Suppose we want to determine:

```text
What percentage of rich people are happy?
```

This can be expressed mathematically as:

```text
P(Happy | Rich)
```

which means:

```text
Probability that a person is happy
given that the person is rich.
```

---

# Applying Bayes Theorem

Bayes Theorem states:

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

For this problem:

```text
A = Happy

B = Rich
```

Therefore:

```text
P(Happy | Rich)

=

[P(Rich | Happy) * P(Happy)]

/

P(Rich)
```

---

# Understanding the Components

To calculate:

```text
P(Happy | Rich)
```

we need three values:

### P(Happy)

The probability that a randomly selected person is happy.

---

### P(Rich)

The probability that a randomly selected person is rich.

---

### P(Rich | Happy)

The probability that a person is rich given that they are happy.

---

# Solution Strategy

The process follows these steps:

### Step 1

Identify the known probabilities.

---

### Step 2

Substitute the known values into Bayes Theorem.

---

### Step 3

Perform the calculations.

---

### Step 4

Interpret the result as:

```text
P(Happy | Rich)
```

which represents the percentage of rich people who are happy.

---

# Why This Example Matters

Many real-world questions cannot be answered directly from the available data.

Instead, we often know:

```text
P(Rich | Happy)
```

but want to determine:

```text
P(Happy | Rich)
```

Bayes Theorem provides the mathematical relationship needed to convert one probability into the other.

---

# Real-World Applications

This same process is used in many machine learning and statistical applications.

### Medical Diagnosis

```text
P(Disease | Positive Test)
```

---

### Fraud Detection

```text
P(Fraud | Suspicious Transaction)
```

---

### Spam Detection

```text
P(Spam | Email Features)
```

---

### Risk Analysis

```text
P(Event | New Information)
```

---

### Recommendation Systems

```text
P(User Preference | User Activity)
```

---

# Conditional Probability Review

The focus of this exercise is conditional probability.

Conditional probability answers questions such as:

```text
What is the probability that an event occurs
given that another event has already occurred?
```

Notation:

```text
P(A|B)
```

Read as:

```text
Probability of A given B
```

---

# Relationship to Machine Learning

Bayes Theorem serves as the foundation for:

```text
Naive Bayes
```

and

```text
Gaussian Naive Bayes
```

classification algorithms.

These algorithms use observed evidence to estimate the probability that a record belongs to a particular class.

Examples include:

- Email Spam Detection
- Medical Classification
- Sentiment Analysis
- Document Classification

---

# Key Takeaways

- Bayes Theorem can be used to calculate the probability of an event given new information.
- The exercise asks: "What percentage of rich people are happy?"
- The desired probability is:

```text
P(Happy | Rich)
```

- Bayes Theorem transforms known probabilities into unknown probabilities.
- Conditional probability is a key concept in statistics and machine learning.
- Many classification algorithms are based on Bayes Theorem.
- Real-world applications include spam filtering, fraud detection, and medical diagnosis.

---

# Important Formula

## Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

## Rich and Happy Example

```text
P(Happy | Rich)

=

[P(Rich | Happy) * P(Happy)]

/

P(Rich)
```