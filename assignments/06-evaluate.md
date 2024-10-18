# Assignment 6: Auditing Algorithms


__Due: 2023-10-21_

Eligible skills: 
- evaluate level 1
- construct level 2
- summarize, 1,2
- visuailze 1,2


## Related notes

- [](../notes/2023-10-12)
<!-- - [](../notes/2023-03-02) -->


## About the data


We have provided a  copy of [reconstructed version](https://github.com/socialfoundations/folktables) of the [Adult](https://archive.ics.uci.edu/dataset/2/adult) Dataset, which is a popular benchmark dataset for training machine learning models that comes from a [recent paper](https://arxiv.org/abs/2108.04884) about the risks of that dataset.  The classic [Adult](https://archive.ics.uci.edu/dataset/2/adult) dataset tries to predict if a person makes more or less than 50k.  

Researchers reconstructed the Adult dataset with the actual value of the income.  We trained models to predict `income>=$10k`, `income>=$20k` , etc.  We used three different learning algorithms, nicknamed 'LR', 'GPR', and 'RPR' for each target (`>10k`, `>20k` ,..., `>90k`).

- `adult_models_only.csv` has the model's predictions 
- `adult_reconstruction_bin.csv` has the data. 


Both data files have a unique identifier column included.

```{admonition} Think Ahead
Why might the dataset have more samples in it than the model predictions one? 
```

## Complete an audit



Thoroughly audit two rannomdly selected  models.  If you load the `adult_models_only.csv` to `models_df` then the following will give you replicable, but random, two columns
```
import numpy as np
my_num = # pick a number
np.random.seed(my_num)
models_to_audit = np.random.choice( models_df.columns,2)
```

In your audit, use at least three different performance metrics. Compare and contrast performance in those metrics across racial or gender groups.

Include easy to read tables with your performance metrics and interpretations of the model's overall performance and any disparities that could be understood by a general audience.  

Which of the two would you think is better to deploy?


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
