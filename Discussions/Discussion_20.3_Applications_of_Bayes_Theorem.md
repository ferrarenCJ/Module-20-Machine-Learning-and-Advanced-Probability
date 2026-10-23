# Discussion 20.3: Applications of Bayes Theorem

In this example, the goal is to predict the missing Activity value for a student when the conditions are:

- Deadline = Near
- Party = No
- Lazy = Yes

Using Naive Bayes classification, we calculate the posterior probabilities for each possible activity:

- Party
- Study
- Pub
- TV

The predicted activity is the class with the highest posterior probability, which is known as Maximum A Posteriori (MAP) estimation.

One challenge in this dataset is that some feature combinations do not appear for every class. For example, certain activities may never occur with a particular combination of deadline, party, and lazy values. When this happens, the conditional probability becomes zero. Because Naive Bayes multiplies probabilities together, a single zero probability causes the entire posterior probability for that class to become zero, regardless of the evidence from other features.

To address this issue, probability smoothing is applied. Instead of assigning a probability of zero to unseen events, a very small value is used. A common approach is Laplace smoothing, which adds a small count to every possible outcome before calculating probabilities. This prevents any probability from becoming exactly zero and allows all classes to remain candidates during classification.

Smoothing changes the computation by ensuring that rare or previously unseen feature combinations still contribute to the final probability calculation. Without smoothing, classes with one unseen feature would be automatically eliminated, even if other evidence strongly supports them. With smoothing, the model can make a more balanced prediction and generalize better to new observations.

After computing the posterior probabilities for all four activity classes and applying MAP estimation, the activity associated with the highest posterior probability would be selected as the prediction for the missing value. This demonstrates how Bayes Theorem and Naive Bayes classification can be used not only for binary classification problems such as spam detection, but also for multi-class prediction problems involving several possible outcomes.