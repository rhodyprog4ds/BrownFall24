---
substitutions:
  accept_assignment: |
    [Template repo for submission](https://classroom.github.com/a/ttGG2ZCa)
  date : 2023-02-14
---

# Assignment 3: Exploratory Data Analysis

__Due:{{ date }} __

{{ accept_assignment }}

```{important}
You have the option to work with a partner. You must plan this in advance so that you have access to collaborate. If you did not find a partner in class and you would like one, try to find one [on the class discussion](https://github.com/rhodyprog4ds/sp23-discuss-sp23community/discussions). @brownsarahm if you do not get a reply. 
```


## Objective & Evaluation

This week your goal is to do a small exploratory data analysis for two datasets of your choice.

Eligible skills: (links to checklists)
-  process [1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#process-level1)
- access [1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#access-level1) and [2](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#access-level2)
- **first chance** summarize [1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#summarize-level1) and [2](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#summarize-level2)
- **first chance** visualize [1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#visualize-level1) and [2](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#visualize-level2)



## Related notes

- [](../notes/2023-02-07)
- [](../notes/2023-02-09)



## Choose Datasets

Each Dataset must have at least three variables, but can have more. Both datasets
must have multiple types of variables. These can be datasets you used last week,
if they meet the criteria below.

### Dataset 1 (d1)

must include at least:
- two continuous valued variables **and**
- one categorical variable.

```{hint}
a dataset from the UCI data repository that's for classification and has continuous features would work for this
```

### Dataset 2 (d2)

must include at least:
- two categorical variables **and**
- one continuous valued variable


## EDA

Use a separate notebook for each dataset, name them `dataset_01.ipynb` and `dataset_02.ipynb`.

For **each** dataset, in the corresponding notebook complete the following:

1. Load the data to a notebook as a `DataFrame` from url or local path, if local, include the data file in your repository.
1. Explore the dataset in a notebook enough to describe its structure use the heading `## Description`

    - shape
    - columns
    - variable types
    - overall summary statisics
1. Write a short description of what the data contains and what it could be used for
2. Include overall summary for the data and interpret what that means. This should include code that generates the statistical summary and sentences in English in a markdown cell with your conclusions and explanation of the statistical summary. Are there limitations in how to safely interpre the data that the summary helps you see? are the variables what you expect? 
3. Ask and answer 3 questions by using and interpreting statistics and visualizations as appropriate. Include a heading for each question using a markdown cell and H2:`##`. Make sure your analyses meet the criteria in the check lists below. Use the checklists to think of what kinds of questions would use those type of analyses and help shape your questions. 
4. Describe what, if anything might need to be done to clean or prepare this data for further analysis in a finale `## Future analysis` markdown cell in your notebook.


### Question checklist

be sure that every question (all six, 3 per dataset) has:
- a heading
- at least 1 statistic or plot
- interpretation that answers the question



### Dataset 1 Checklist
make sure that your `dataset_01.ipynb` has:


- Overall summary statistics grouped by a categorical variable
-  A single statistic grouped by a categorical variable
- at least one plot that uses 3 total variables
-  a plot and summary table that convey the same information. This can be one statistic or many.



### Dataset 2 Checklist
make sure that your `dataset_02.ipynb` has:

- overall summary statistics
- two individual summary statistics for one variable
- one summary statistic grouped by two categorical variables
- a figure with a grid of subplots that correspond to two categorical variables



```{tip}
Be sure to start early and use help hours to make sure you have a plan for all of these.
```

## Peer Review

```{note}
This is optional, but if you do a review, you only need to do one analysis each.
```


With a partner (or group of 3 where person 1 review's 2 work, 2 reviews 3, and 3 reviews 1) read
your partner's notebook and complete a peer review on their pull request.  You can do peer review
when you have done most of your analysis, and explanation, even if some parts of the code do not
work.

In your review:
- Use inline comments to denote places that are confusing or if you see solutions to problems your classmate could not solve
- Use the template below for your summary review

### Review Questions


1. How was the analysis overall to read? easy? hard? cohesive? jumpy?
1. Did the data summaries tell you enough about the data to understand the analysis and anticipate what kinds of questions could be answered? If not, what questions do you still have about the data?
1. Do the questions make sense based on the data? Are they interesting questions? What could improve the questions
1. Are the statistics and plots appropriate for the questions?
1. Are the interpretations complete, clear, and consistent with the statistics and plots?
1. What could be done to make the explanations more clear and complete?
1. What additional analysis might make the analysis more compelling and clear?


```
<!-- delete sections that are not needed -->
## Overall  

This analysis was ...

## Data Summaries

- [ ] complete

To understand this analysis I still need to know ...

## Checklist

- [ ] questions fit the data
- [ ] questions are in natural language
- [ ] chosen statistics and plots match questions
- [ ] all statistics and plots have an interpretation in English

## Areas of improvement

```


### Response

Respond to your review either inline comments, replies, or by updating your analysis accordingly.



````{margin}
```{warning}
This section is not required, but is intended to help you get started thinking
about ideas for your portfolio.  If you complete it, we'll give your feedback to
help shape your ideas to get to level 3 achievements.  If you want to focus only
on level 2 at this moment in time, feel free to skip this part.
```
````

```{admonition} Think Ahead
1. How could you make more customized summary tables?
1. Could you use any of the variables in this dataset to add more variables that would make interesting ways to apply split-apply-combine? (eg thresholding a continuous value to make a categorical value)
```
