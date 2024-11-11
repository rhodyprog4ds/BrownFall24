# Assignment 7: Classification

[accept the assigment](https://classroom.github.com/a/q-cpZN-M)

__Due: 2023-10-28__

 
Eligible skills: 
- evaluate level 2
- classification level 1,2
- summarize, 1,2
- visuailze 1,2

## Related notes

- [](../notes/2024-10-17)
<!-- - [](../notes/2023-10-19) -->

::::{important}
There is a large extra section in the notes, that should be of use for this assignment. 

You can use Gassian Naive Bayes **or** a Decision tree for the assignment. 
::::

## Dataset and EDA


Choose a dataset that is well suited for classification and that has *all numerical features*.
If you want to use a dataset with nonnumerical features you will have to convert
the categorical features to numerical with one hot encoding.  

```{hint}
Use the [UCI ML repository](https://archive.ics.uci.edu/datasets), it  will let you filter data by the attributes of it you need. 
```

1. Include a basic description of the data(what the features are)
1. Describe the classification task in your own words
1. Use EDA to determine if you expect the classification to get a high accuracy or not. What types of mistakes do you think will happen most (think about the confusion matrix)? 
1. Hypothesize which classifier from the notes will do better and why you think that. Does the data meet the assumptions of Naive Bayes? What is important about this classifier for this application? 

```{important}
 You will get to reuse the above, and this dataset, for the clustering assignment *and* optionally one or both of A10 and A11. 
```

## Basic Classification

1. Fit your chosen classifier with the default parameters on 80% of the data
1. Inspect the model to answer the questions appropriate to your model.

    - Does this model make sense?
    - (if DT) Are there any leaves that are very small?
    - (if DT) Is this an interpretable number of levels?
    - (if GNB) do the parameters fit the data well? or do the paramters generate similar synthetic data (you can answer statistically only or with synthetic data & a plot)
1. Test it on 20% held out data and generate a classification report
2. Interpret the model and its performance in terms of the application in order to give a recommendation, "would you deploy this model" . Example questions to consider in your response include

  - do you think this model is good enough to use for real?
  - is this a model you would trust?
  - do you think that a more complex model should be used?
  - do you think that maybe this task cannot be done with machine learning?

:::{note}
You need to give a thorough answer to the deployment question and these bulleted questions will help you create a thorough response. 
:::

## Exploring Problem Setups

```{important}
Understanding the impact of test/train size is a part of classifcation and helps with evaluation.  This exercise is *also* a chance at python level 2.
```

````{margin}
```{tip}
The summary statistics and visualization we used before are useful for helping to
investigate the performance of our model.  We can try fitting a model  with different settings
to create a new "dataset" for our experiments.
The same skills apply.
```


```{hint}
The most important thing about the max depth here is that it's the same across all of the models. If you get an error, try making it smaller.
```

````
Do an experiment to compare test set size vs performance:
1. Use a loop to train a model  on 10%, 30%, ... , 90% of the data. Compute the {term}`training accuracy` and test accuracy for each size training data. Create a DataFrame with columns ['train_pct','n_train_samples','n_test_samples','train_acc','test_acc']
2. Use EDA on this data frame to interpret the results of your experiment.  How does training vs test size impact the model's performance? Does it impact training and test accuracy the same way? 


```{warning}
Please make sure you complete the above and get feedback before you go on to
the following, because if you attempt the following with an error in the above
you may spend a lot of time on something that might not earn credit
```

:::::{margin}
:::{note}
This also will extend on visualize and summarize. 

See the [seaborn error bars tutorial](https://seaborn.pydata.org/tutorial/error_bars.html)
:::
::::

```{admonition} Thinking Ahead
_ideas for level 3 evaluate, not required for A7_

Repeat the problem setup experiment with multiple test/train splits at each size and plot with {term}`error bars`.
- What is the tradeoff to be made in choosing a test/train size?
- What is the best test/train size for this dataset?

or with variations:
- allowing it to figure out the model depth for each training size, and recording the depth in the loop as well.  
- repeating each size 10 items, then using summary statistics on that data

Use the extensions above to experiment further with other model parameters.

**some of this we'll learn how to automate in a few weeks, but getting the
ideas by doing it yourself can help build understanding and intution**
```
