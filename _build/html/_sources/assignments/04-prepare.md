---
substitutions:
  accept_assignment: |
    [accept the assignment](https://classroom.github.com/a/X4txYKLU)
  date : 2023-02-21
---
# Assignment 4:

__Due: {{ date }}__

{{ accept_assignment }}


Eligible skills: (links to checklists)
- **first chance** prepare [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#prepare-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#prepare-level2)
- access [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level2)
- python [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level2)
- summarize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level2)
- visualize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level2)



## Related notes

- [](../notes/2023-02-14)
- [](../notes/2023-02-16)


## Check the Datasets you have worked with already

In the datasets you have used or come across but decided you could not work with
 in your past assignments identify at least one
thing you could not do because the data was not in an appropriate format.

Apply one fix and show one summary statistic or plot that was not possible before 
to show that it works.


Some examples:
- a column that was a list
- missing values
- a column that was continuous, but more interesting as a categorical
- too many header rows

```{admonition} Think Ahead

_this box is not required, but ideas for portfolio_
cleaning a dataset to make it able to answer questions that were not possible could satisfy the level 3 prepare requirements.
```


## Clean example datasets

There are notebooks in the template that have instructions for how to work with each dataset, including how to load it and what high level cleaning should be done.  Your job is to execute.

To earn prepare level 2, clean any dataset and do just enough exploratory data analysis to show that the data is usable (eg 1 stat and/or plot).

To *also* earn python level 2: clean the CS degrees dataset (use a function or lambda AND loop or list/dictionary comprehension)

To *also* earn access level 2: clean the airline data (to get data in a second file type).

To *also* earn summarize and/or visualize level 2: add extra exploratory data analyses of your cleaned dataset meeting the criteria from the checklist (eg follow a3 checklists).


This means that if you want to earn prepare, python, and access, you will need to clean two datasets.

```{hint}
renaming things is often done well with a dictionary comprehension or lambda.
```

## Study Cleaned Datasets

Read example data cleaning notes or scripts. To do this find at least one dataset for which the messy version, clean version, and a script or notes about how it was cleaned are available, answer the following questions in a markdown file or additional notebook in your repository. (some example datasets are on the datasets page and one is in the notes are added to the course website)

1. What are 3 common problems to look for in a dataset? Describe them with examples. 
1. Using one of the examples you found of cleaned data, give an example of a question or context that would require making different choices than were made. Include a bit about the data, what was done, the question, what would need to be done instead and justification.
1. Explain in your own words, with a concrete example, how domain expertise can help you when cleaning data. Use either a made up example or one that you read about.

```{warning}
Some of these examples have both the clean and messy data files and an R script to do the cleaning. You are not required to *know* R, but looking at their R cleaning script could give hints of what things they fixed or changed. You could also compare the clean and messy versions by looking at them with a tool of your choice. 
```

```{important}
Remember to run the ["Submit" Workflow](submitaction) from the actions tab of your repository. [see how on the How tos page](submitaction)
```