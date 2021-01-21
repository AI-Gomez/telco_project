## Telco Churn

Angel Gomez 09/23/2020

# Goal
* The goal of the project is to find the drivers for churn at Telco and create a model to predict churn.

### Project Planning

# First Thoughts
* Overall churn rate is at 26% however there are many factors that contribute to churn.

# Hypothesis
Is Tech Support a factor in Churn?
* After utilizing the exploration data, it seems there may be a relationship with tech support and churn. 

Do fiber optic customers have a higher rate of churn?
* A relationship with fiber customers and churn may exist after plotting the exploration data.

# acquire.py
* Creating an acquire.py allows us to acquire data from the telco_churn sql database hosted on the codeup server. 

# prepare.py
* The prepare.py hosts our helper functions and other prep code to be implemented in our jupyter notebooks.

# Exploration
* By plotting data, we can see any relationships that exist with customer churn.

# Model and Evaluation
* Creating a baseline in this stage notifies us if a model is deemed successful by achieving a higher accuracy score. After a baseline has been established, we can now utilize sklearn's train, validate, and test to try out models and see which one performs the best.

# Summary
* A summary of our findings and a prediction model in the form of a csv file is included in the summary.

# Data Dictionary
* Churn Rate: Rate of Customers that seize to do busines with that specific entity.
* Null Hypothesis:  the hypothesis that there is no significant difference between specified populations, any observed difference being due to sampling or experimental error.
* Alternative Hypothesis: This hypothesis is contrary to the null hypothesis.
* P-Value: Assuming the null hypothesis is correct, the p value is the probability of obtaining results as close to the hyptohesis results.
* Logistic Regression Model: a model used when the target variable is categorical.
* Decision Tree Model:an 'if, else' tree sctructed model.
* Random Forest Model: a model that consists of many 'decision trees' from the decision tree model.
* KNN Model: K nearest Neighbors is a model that stores all data and classifies new data based on a correlation with old data.
* Confusion Matrix: a visialization that displays the performance of an algorythm.
* Classification Report: Used to measure the quality of the algorythm.
* Accuracy: ratio of number of correct predictions.
* F1-Score: the average between precision and recall
* Precision: The number of correct positive results
* Recall: correct positive results dived by the number of all relevant samples.


