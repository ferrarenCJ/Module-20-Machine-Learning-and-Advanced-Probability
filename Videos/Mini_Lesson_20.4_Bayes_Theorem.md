# Mini-Lesson 20.4: Bayes Theorem

## Overview

Bayes Theorem is one of the most important concepts in probability theory and machine learning. It is used to calculate conditional probability, which is the probability of an event occurring given that another related event has already occurred.

Bayes Theorem provides a mathematical framework for updating probabilities when new information becomes available. Many machine learning algorithms, including Naive Bayes and Gaussian Naive Bayes, are built upon this principle.

---

# Introduction to Bayes Theorem

Bayes Theorem is used to determine the probability of an event occurring given that another event has already occurred.

Given two events:

```text
A and B
```

the conditional probability is represented as:

```text
P(A|B)
```

which means:

```text
Probability of A occurring given that B has occurred
```

Bayes Theorem is particularly useful when outcomes depend partially on prior events or observations.

---

# Real-World Example

Imagine there are three bags containing different combinations of coins.

A coin is selected from a randomly chosen bag, and the coin turns out to be a quarter.

Bayes Theorem can help answer the question:

```text
What is the probability that the coin came from Bag 1?
```

This type of reasoning appears frequently in:

- Spam detection
- Medical diagnosis
- Fraud detection
- Recommendation systems
- Risk analysis

---

# Bayes Theorem Formula

Bayes Theorem is written as:

```text
P(A|B) = [P(B|A) * P(A)] / P(B)
```

Where:

```text
P(A|B)
```

Probability of A given B

```text
P(B|A)
```

Probability of B given A

```text
P(A)
```

Prior probability of A

```text
P(B)
```

Probability of B

---

# Proof of Bayes Theorem

The proof begins with the probability of two events occurring simultaneously.

## Step 1

The joint probability of events A and B can be written as:

```text
P(A ∩ B) = P(A) * P(B|A)
```

This means:

```text
Probability of A occurring
multiplied by
Probability of B occurring given A
```

### Ice Cream Example

Suppose:

```text
A = Store has ice cream in stock

B = You finish the entire ice cream cone
```

Then:

```text
P(A ∩ B)
```

represents the probability that:

- The store has ice cream available
- You finish the entire ice cream cone

---

## Step 2

The same joint probability can also be written as:

```text
P(A ∩ B) = P(B) * P(A|B)
```

---

## Step 3

Since both expressions equal:

```text
P(A ∩ B)
```

they may be set equal to one another:

```text
P(A) * P(B|A)

=

P(B) * P(A|B)
```

---

## Step 4

Divide both sides by:

```text
P(B)
```

Result:

```text
P(A|B)

=

[P(B|A) * P(A)] / P(B)
```

This produces the standard Bayes Theorem equation.

---

# Extension of Bayes Theorem

In many real-world problems there are multiple possible events rather than only two.

The theorem can therefore be extended to account for all possible explanations for an observed event.

Suppose:

```text
A1, A2, ..., An
```

represent all possible outcomes.

Then:

```text
P(B)
```

can be rewritten as:

```text
P(B)

=

Σ P(B|Ai) * P(Ai)
```

where the summation runs across all possible events.

This allows Bayes Theorem to be written as:

```text
P(Ai|B)

=

[P(B|Ai) * P(Ai)]

/

Σ P(B|Aj) * P(Aj)
```

This form is commonly used in machine learning classification algorithms.

---

# Example: Poker Chip Problem

Suppose two bags contain poker chips.

## Bag 1

```text
7 Red Chips
2 Blue Chips
```

Total:

```text
9 Chips
```

---

## Bag 2

```text
5 Red Chips
9 Blue Chips
```

Total:

```text
14 Chips
```

---

## Define Events

Let:

```text
B1
```

represent the event that the chip came from Bag 1.

Let:

```text
B2
```

represent the event that the chip came from Bag 2.

Let:

```text
R
```

represent the event of drawing a red chip.

---

## Known Probabilities

Probability of drawing a red chip from Bag 1:

```text
P(R|B1)

=

7 / 9
```

Probability of drawing a red chip from Bag 2:

```text
P(R|B2)

=

5 / 14
```

---

## Goal

Determine:

```text
P(B1|R)
```

which represents:

```text
Probability the chip came from Bag 1
given that the chip is red
```

---

## Apply Bayes Theorem

```text
P(B1|R)

=

[P(R|B1) * P(B1)]

/

[P(R|B1) * P(B1) + P(R|B2) * P(B2)]
```

After substituting the values and simplifying:

```text
P(B1|R)

≈ 0.685
```

---

## Final Result

```text
68.5%
```

There is a 68.5% probability that a red poker chip came from Bag 1.

---

# Why Bayes Theorem Matters

Bayes Theorem allows probabilities to be updated using new evidence.

It provides a mathematical framework for:

- Decision making under uncertainty
- Predictive modeling
- Classification algorithms
- Probabilistic machine learning

---

# Applications in Machine Learning

## Spam Detection

Determine the probability that an email is spam.

---

## Medical Diagnosis

Estimate the likelihood of a disease given symptoms or test results.

---

## Financial Fraud Detection

Estimate whether a transaction is fraudulent.

---

## Recommendation Systems

Predict user preferences and behaviors.

---

## Risk Assessment

Estimate probabilities of uncertain events.

---

# Relationship to Naive Bayes

Bayes Theorem serves as the mathematical foundation for:

```text
Naive Bayes
```

and

```text
Gaussian Naive Bayes
```

These machine learning algorithms use Bayes Theorem to classify observations based on probabilities.

The following lessons build directly upon the concepts introduced here.

---

# Key Takeaways

- Bayes Theorem is used to calculate conditional probabilities.
- Conditional probability measures the likelihood of an event given new evidence.
- Bayes Theorem updates prior beliefs using observed information.
- The theorem can be extended to problems involving multiple possible events.
- Bayes Theorem is the foundation of Naive Bayes and Gaussian Naive Bayes classifiers.
- Common applications include spam filtering, fraud detection, medical diagnosis, and recommendation systems.

---

# Important Formulas

## Conditional Probability

```text
P(A|B)
```

---

## Bayes Theorem

```text
P(A|B)

=

[P(B|A) * P(A)]

/

P(B)
```

---

## Extended Bayes Theorem

```text
P(Ai|B)

=

[P(B|Ai) * P(Ai)]

/

Σ P(B|Aj) * P(Aj)
```