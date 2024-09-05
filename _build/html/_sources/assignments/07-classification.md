# Assignment 7

[accept the assigment (link tbd)]()

__Due: TBA__

Eligible skills: (links to checklists)


- **first chance** classification [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#classification-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#classification-level2)
- evaluate [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#evaluate-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#evaluate-level2)
- summarize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level2)
- visualize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level2)
- python [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level2)

## Related notes

- [](../notes/2023-03-07)
- [](../notes/2023-03-09)


## Dataset and EDA


Choose a datasets that is well suited for classification and that has all numerical features.
If you want to use a dataset with nonnumerical features you will have to convert
the categorical features to one hot encoding.  

```{hint}
Use the UCI ML repository
```

1. Include a basic description of the data(what the features are)
1. Describe the classification task in your own worlds
1. Use EDA to determine if you expect the classification to get a high accuracy or not. What types of mistakes do you think will happen most? 
1. Explain why or why not Gaussian Naive Bayes and Decision Trees are a reasonable model to try for this data.
1. Hypothesize which will do better and why you think that.


## Basic Classification

1. Fit your chosen classifier with the default parameters on 50% of the data
1. Test it on 50% held out data and generate a classification report
1. Inspect the model to answer the questions appropriate to your model.

    - Does this model make sense?
    - (DT) Are there any leaves that are very small?
    - (DT) Is this an interpretable number of levels?
    - (GNB) do the parameters fit the data well?
    - (GNB) do the paramters generate similar synthetic data
1. Repeat the split, train, and test steps 5 times, save the scores into a dataframe. Compute the mean and std of the scores.

    - Is the performance consistent enough you trust it?
1. Interpret the model and its performance in terms of the application. Example questions to consider in your response include

  - do you think this model is good enough to use for real?
  - is this a model you would trust?
  - do you think that a more complex model should be used?
  - do you think that maybe this task cannot be done with machine learning?


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
1. Train a model (if decision tree set the max depth 2 less than the depth it found above) on 10%, 30%, ... , 90% of the data. Compute the {term}`training accuracy` and test accuracy for each size training data in a DataFrame with columns ['train_pct','n_train_samples','n_test_samples','train_acc','test_acc']
1. Plot the accuracies vs training percentage in a line graph.  
1. Interpret these results.  How does training vs test size impact the model?

_use a loop for this part, possibly also a function_



```{admonition} Thinking Ahead
_ideas for level 3_

Repeat the problem setup experiment with cross validation and plot with error bars.
- What is the tradeoff to be made in choosing a test/train size?
- What is the best test/train size for this dataset?

or with variations:
- allowing it to figure out the model depth for each training size, and recording the depth in the loop as well.  
- repeating each size 10 items, then using summary statistics on that data

Use the extensions above to experiment further with other model parameters.

**some of this we'll learn how to automate in a few weeks, but getting the
ideas by doing it yourself can help build understanding and intution**
```
