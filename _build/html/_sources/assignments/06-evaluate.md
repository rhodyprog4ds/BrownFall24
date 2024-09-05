---
substitutions:
  accept_assignment: |
    [accept the assignment](https://classroom.github.com/a/pJ-8jn5f)
  date : 2023-03-09
---

# Assignment 6: Auditing Algorithms

[accept the assignment](https://classroom.github.com/a/pJ-8jn5f)
__Due: 2023-03-09__

Eligible skills: (links to checklists)

````{margin}
```{important}
the definition for evaluate is going to be updated in your gradetrackers soon, the version on the site is correct
```
````
- **first chance** evaluate [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#evaluate-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#evaluate-level2)
- construct [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#construct-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#construct-level2)
- summarize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level2)
- visualize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level2)
- python [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level2)



## Related notes

- [](../notes/2023-02-28)
- [](../notes/2023-02-02)


## About the data


We have provided a version of the [Adult] Dataset, which is a popular benchmark dataset for training machine learning models that comes from a recent paper about the risks of that dataset.  The classic Adult dataset tries to predict if a person makes more or less than 50k.  

Researchers reconstructed the Adult dataset with the actual value of the income.  We trained models to predict `income>=$10k`, `income>=$20k` , etc.  We used three different learning algorithms, nicknamed 'LR', 'GPR', and 'RPR' for each target.

`adult_models_only.csv` has the model's predictions and `adult_reconstruction_bin.csv` has the data. Both have a unique identifier column included.

```{admonition} Think Ahead
Why might the dataset have more samples in it than the model predictions one?
```

## Complete an audit


Thoroughly audit any one model.  In your audit, use three different performance metrics. Compare and contrast performance in those metrics across both racial or gender groups.

Include easy to read tables with your performance metrics and interpretations of the model's overall performance and any disparities that could be understood by a general audience.  

If the model you chose was used for some real world decision what might the risks be?


## Extend your Audit

```{note}
optional
(for more Achievements or deeper understanding/more practice)
```

Use functions and loops to build a dataset about the performance of the different models so that you can answer the following questions:

1. Which model (target and learning algorithm) has the best accuracy?
1. Which target value has the least average disparity by race? by gender?
1. Which learning algorithm has the least average disparity by race? by gender?
1. Which model (target and learning algorithm) do you think is overall the best?


```{list-table} Example table format

* - y
  - model
  - score
  - value
  - subset
* - >=10k
  - LR
  - accuracy
  - .873
  - overall
* - >=20k
  - RPR
  - false_pos_rate
  - .873
  - men
```

This table is not real data, just headers with one example value to help illustrate what the column name means.


```{hint}
This step you should make separate data frames and then merge them together for construct. If you don't need construct you can build it as one, for visualize you should use appropriate groupings
```
