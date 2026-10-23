# Self-Study Discussion 20.1: Thinking Like a Data Scientist - Introduction to Machine Learning and Advanced Probability

One resource that I found especially helpful during this module was the Scikit-Learn User Guide:

https://scikit-learn.org/stable/user_guide.html

The Scikit-Learn documentation helped me better understand how machine learning algorithms are implemented in practice. Throughout Module 20, we worked with Naive Bayes classifiers, Gaussian Naive Bayes, train-test splits, and model evaluation. The examples and explanations in the User Guide made it easier to understand the general machine learning workflow of preparing data, training a model, generating predictions, and evaluating results.

Another resource that I found valuable was the UCI Machine Learning Repository:

https://archive.ics.uci.edu/

The repository provides many real-world datasets, including the SMS Spam Collection dataset used in our spam detection activities. Exploring the datasets and associated documentation helped me understand how machine learning models are applied to practical classification problems.

One tip that helped me complete the coding activities and final assignment was using small validation checks throughout the notebook. Before training a classifier, I would verify data types, dataset shapes, and sample records using functions such as:

```python
df.shape
df.head()
df.info()
```

This helped identify issues early, such as incorrect label encoding, missing values, or mismatched training and testing data sizes.

Finally, I found that drawing simple diagrams for Bayes Theorem and Naive Bayes calculations made the probability concepts easier to understand. Visualizing conditional probabilities and classification decisions helped me connect the mathematical formulas to their real-world applications in spam detection and machine learning classification.

As I continue through the program, I plan to bookmark these resources and maintain a personal knowledge repository that includes useful documentation, datasets, code snippets, and study notes for future machine learning and data engineering projects.