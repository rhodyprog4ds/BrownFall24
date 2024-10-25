
# Assignment 8: Clustering

__Due: 2024-11-04__

## Evaluation

Eligible skills: (links to checklists)
- clustering 1
- evaution 1,2
- visualize 1,2
- summarize 1,2

_for some of these you will need to add analysis that is not described in the instructions below, but is related to this and that skill_

## Related notes


- [](../notes/2024-10-22)
- [](../notes/2024-10-24)



## Instructions

Use the same dataset you used for assignment 7, unless there was a problem. If you skipped assignment 7, choose a dataset well suited for classification. See A7 for tips. 

1. Describe what question you would be asking in applying clustering to this dataset. What does it mean if clustering does not work well? 
2. How does this task compare to what the classification task on this dataset?
3. Apply Kmeans using the known, correct number of clusters, $K$.
4.  Evaluate how well clustering worked on the data:

    - using a true clustering metric and
    - using visualization and
    - using a clustering metric that uses the ground truth labels
5. Include a discussion of your results that addresses the following:

    - describes what the clustering means
    - what the metrics show
    - Does this clustering work better or worse than expected based on the classification performance (if you didn't complete assignment 7, also apply a classifier)
6. Repeat your analysis using a 2 different numbers (1 higher, one lower) of clusters:

    - can you interpret the new clusters?
    - how do they relate to the original clusters? are they completely different, did one split?
    - is there a reasonable explanation for more or less clusters than there are classes in this dataset?

<!-- 
## For classification

```{warning}
Do this only if you did not already earn classification level 2
```

1. Fit your chosen classifier with the default parameters on 50% of the data
1. Test it on 50% held out data and generate a classification report
1. Inspect the model to answer the questions appropriate to your model.

    - Does this model make sense?
    - (if DT) Are there any leaves that are very small?
    - (if DT) Is this an interpretable number of levels?
    - (if GNB) do the parameters fit the data well?
    - (if GNB) do the paramters generate similar synthetic data
1. Interpret the model and its performance in terms of the application. Example questions to consider in your response include

  - do you think this model is good enough to use for real?
  - is this a model you would trust?
  - do you think that a more complex model should be used?
  - do you think that maybe this task cannot be done with machine learning? -->
