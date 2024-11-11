# Assignment 9:  Regression and Optimization


__Due: 2024-11-15__

```{important}
Since this is posted late you can do regression and optimize together
*or* you can do only the regression part of this assigment and focus on optimization for classification or clustering in A10 while **also** doing model comparison. 

If you optimize a regression model other than LASSO, we will evaluate it for regresion level 3. 
```

## Assessment

Eligible skills: (links to checklists)

- process
- regression
- evaluate
- optimize

## Related notes

- [](../notes/2024-10-29)
- [](../notes/2024-10-31)
- [](../notes/2024-11-06)


## Instructions

Find a dataset suitable for regression. We recommend a dataset from the UCI repository. Remember that you can use the filters to choose a dataset that is well-suited for regression. 

### Linear Regression Basics

TLDR: Fit a linear regression model, measure the fit with two metrics, and make a plot that helps visualize the result.

1. Include a basic description of the data(what the features are, units, size of dataset, etc)
2. Write  your own description of what the prediction task it, why regression is appropriate.
3. Fit a linear model on all numerical features with 75% training data.
4. Test it on 25% held out test data and measure the fit with two metrics and one plot
5. Inspect the model to answer:

    - What to the coefficients tell you?
    - What to the residuals tell you?
6. Repeat the split, train, and test steps 5 times.

    - Is the performance consistent enough you trust it?
7. Interpret the model and its performance in terms of the application. Some questions you might want to answer in order to do this include:

  - do you think this model is good enough to use for real?
  - is this a model you would trust?
  - do you think that a more complex model should be used?
  - do you think that maybe this task cannot be done with machine learning?
1. Try fitting the model only on one feature. Justify your choice of feature based on the results above.  Plot this result.

### Optimize a more complex regression model


1. Choose a different regression model based on the structure of your data and the performance of the basic linear regression on both all features and a single feature. This could be LASSO, [DecisionTreeRegression](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html), [SVR regression](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html) (note that at these links there are examples so you can learn about them by looking at data they excel on)
2. Fit and score this model with the default parameters
3. Choose reasonable model parameter values for your parameter grid by assessing how well the model fit with the default values.
4. Use grid search to find the best performing model parameters.
5. Examine the best fit model, how different is it from the default
6. Score the best fit model on a held out test set.
7. Examine and interpret the cross validation results. How do they vary in terms of time? Is the performance meaningfully different or just a little?
8. Try varying the cross validation parameters (eg the number of folds and/or type of cross validation). Does this change your conclusions?

