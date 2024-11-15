
# Assignment 11: Model Comparison

## Quick Facts
<!-- -  [accept the assignmnt](https://classroom.github.com/a/Rw_yt2rK) -->
- __Due: 2024-11-22__

## Related notes

- [](../notes/2024-11-12)
- [](../notes/2024-11-14)

## Assessment

Eligible skills: 
- compare
- optimize
- evaluate
- (one of) regression, classification, clustering
- summarize
- visualize


:::{tip}
The next assignment will focus on a categorical outcome, so if you did not complete A9, use regression for this assignment. 

The next assignment can use either, but classification will be less for for A11, so clustering might be a good choice for this assignment i fyou have not earned that yet. 
:::

## Instructions




```{tip}
this is best for regression or classification, but if you use clustering
use the `scoring` parameter to pass better metrics than the default
of the score method.
```

```{hint}
See the questions to consider in A9 for more detail on what to consider when optimizing each model. 

If you are skipping submitting A9, follow those instructions for each model. 
```

Choose a dataset, it can be appropriate for classification, regression, or clustering. Optimize at least two models for the same task and choose the appropriate metrics to compare the fit. Decide which model you would recommend based on a realistic setting for that dataset and include evidence justifying that choice. Summarize your findings with plots and tables as appropriate.

You can reuse a dataset you've used for one of the previous assignments or choose a new dataset.

```{admonition} Think Ahead

How would this decision making compare for a more complex model or in more realistic setting.

```

## Collaborative Version

Use the [template repo and join a team with your selected partner](https://classroom.github.com/a/CKymxRHg)

First in either a notebook or a python file, split the data into train and test sets and save each to a separate csv. 

In the shared repo, each student should use the training data to optimize one model, evaluating the result somewhat and explaining its general strengths and weaknesses.  Then save the results of the optimization with at least 50 total parameter options to a csv and [export the best model](https://scikit-learn.org/stable/model_persistence.html#skops-io)

In a third notebook, load both optimization datasets and models and then compare the two thoroughly. 


