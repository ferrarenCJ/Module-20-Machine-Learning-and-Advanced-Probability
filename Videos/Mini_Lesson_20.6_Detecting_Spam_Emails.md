# Mini-Lesson 20.6: Detecting Spam Emails

## Overview

In Video 20.8, Naive Bayes Theorem was introduced as a method for classifying emails as either:

- Normal (Non-Spam)
- Spam

This lesson demonstrates how Naive Bayes can be applied to a real-world spam detection problem by using word frequencies and conditional probabilities.

The goal is to determine the probability that an email belongs to a particular category based on the words it contains.

---

# Email Classification Using Naive Bayes

Naive Bayes is a probabilistic classification algorithm that estimates:

```text
P(Class | Features)
```

For spam filtering, the classes are:

```text
Normal
```

and

```text
Spam
```

The features are typically words or phrases that appear in emails.

Examples:

```text
dear
money
password
offer
winner
```

---

# Naive Bayes Formula

The probability that an email belongs to a class is calculated using:

```text
P(Class | Word)

=

[P(Word | Class) * P(Class)]

/

P(Word)
```

Where:

```text
P(Class | Word)
```

Posterior probability that the email belongs to a class given a word.

```text
P(Word | Class)
```

Likelihood of observing the word within the class.

```text
P(Class)
```

Prior probability of the class.

```text
P(Word)
```

Overall probability of observing the word.

---

# Example Dataset

Suppose there are:

```text
50 Total Emails
```

classified as:

```text
30 Normal Emails
20 Spam Emails
```

---

# Step 1: Calculate Prior Probabilities

## Probability of Normal Email

```text
P(Normal)

=

30 / 50

=

0.60
```

---

## Probability of Spam Email

```text
P(Spam)

=

20 / 50

=

0.40
```

---

# Word Frequencies

The Normal and Spam emails contain different words with different frequencies.

---

## Normal Email Words

Common words found in Normal emails:

```text
dear
money
```

Frequency counts:

```text
dear  = 30 occurrences
money = 5 occurrences
```

---

## Spam Email Words

Common words found in Spam emails:

```text
password
money
```

Frequency counts:

```text
password = 10 occurrences
money    = 20 occurrences
```

---

# Step 2: Calculate Word Likelihoods

## Word "Money" Given Normal Email

The word:

```text
money
```

appears:

```text
5 times
```

within:

```text
30 Normal Emails
```

Therefore:

```text
P(Money | Normal)

=

5 / 30

=

0.167
```

---

## Word "Money" Given Spam Email

The word:

```text
money
```

appears:

```text
20 times
```

within:

```text
20 Spam Emails
```

Therefore:

```text
P(Money | Spam)

=

20 / 20

=

1.0
```

---

# Classification Problem

Suppose a new email arrives and contains the word:

```text
money
```

The objective is to determine:

```text
P(Normal | Money)
```

which represents:

```text
Probability that the email is normal
given that it contains the word "money"
```

---

# Applying Naive Bayes

Substitute the values into the Naive Bayes formula:

```text
P(Normal | Money)

=

[P(Money | Normal) * P(Normal)]

/

P(Money)
```

Using the values from the dataset:

```text
P(Money | Normal)

=

5 / 30
```

```text
P(Normal)

=

30 / 50
```

After performing the calculations:

```text
P(Normal | Money)

=

0.30
```

---

# Final Result

```text
P(Normal | Money)

=

0.30
```

Interpretation:

```text
There is a 30% probability
that an email containing the word "money"
is a normal email.
```

Equivalently:

```text
There is a 70% probability
that the email is spam.
```

Based on the data, the word:

```text
money
```

is more strongly associated with spam emails than with normal emails.

---

# Why This Works

Naive Bayes uses historical data to estimate the relationship between words and email categories.

The more frequently a word appears in one class relative to another, the more influence it has on future classifications.

This allows the algorithm to learn patterns such as:

```text
password
→ Spam
```

```text
winner
→ Spam
```

```text
meeting
→ Normal
```

```text
schedule
→ Normal
```

---

# Challenges in Real-World Spam Detection

Real email datasets often contain:

- Millions of emails
- Thousands of unique words
- Large feature sets
- Constantly changing spam tactics

The most computationally expensive step is often building the frequency tables used to estimate probabilities.

Once the probabilities are calculated, classification can be performed efficiently.

---

# Advantages of Naive Bayes for Spam Filtering

## Fast Training

Works efficiently on large datasets.

---

## Low Computational Cost

Requires less processing power than many other machine learning models.

---

## Effective Text Classification

Works well with word-frequency features.

---

## Scalable

Can handle very large collections of emails.

---

# Real-World Applications

## Spam Detection

Classify emails as:

```text
Spam
```

or

```text
Not Spam
```

---

## Fraud Detection

Identify suspicious financial activity.

---

## Document Classification

Assign documents to categories.

---

## Sentiment Analysis

Determine whether text is positive, negative, or neutral.

---

## Medical Diagnosis

Estimate disease probabilities from symptoms.

---

# Key Takeaways

- Naive Bayes is widely used for email spam detection.
- Words are treated as features for classification.
- The algorithm estimates probabilities using Bayes Theorem.
- Historical word frequencies are used to classify future emails.
- In the example, an email containing the word "money" had a 30% probability of being normal.
- Naive Bayes remains one of the most efficient and practical text-classification algorithms.

---

# Important Formula

## Naive Bayes Classification

```text
P(Class | Word)

=

[P(Word | Class) * P(Class)]

/

P(Word)
```

---

## Spam Detection Example

```text
P(Normal | Money)

=

0.30
```

```text
P(Spam | Money)

=

0.70
```