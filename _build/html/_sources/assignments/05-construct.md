---
substitutions:
  accept_assignment: |
    [accept the assignment](https://classroom.github.com/a/Tar0f4BB)
  date : 2023-03-01
---
# Assignment 5: Constructing Datasets and Using Databases

<!-- {{ accept_assignment }} -->

[accept the assignment](https://classroom.github.com/a/Tar0f4BB)

__Due: 2023-03-01__

Eligible skills: (links to checklists)
- **first chance** construct [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#construct-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#construct-level2)
- {fa}`hourglass-end` [^expiringskill] access [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level2)
- {fa}`hourglass-end` [^expiringskill] python [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level2)
- {fa}`hourglass-end` [^expiringskill] prepare [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#prepare-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#prepare-level2)
- summarize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level2)
- visualize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#visualize-level2)


[^starredskill]: skills will be marked like this on the first time they are eligible
[^expiringskill]: skills will be marked like this on the last assignment they are eligible
## Related notes

- [](../notes/2023-02-21)
- [](../notes/2023-02-23)


## Constructing Datasets


Your goal is to programmatically construct two ready to analyze datasets from multiple sources. 

- Each dataset must combine at least 2 source tables(4 total source tables).
- At least one source table must come from a database or from web scraping.
- You should use at least three different joins(types of merges, or concat).

````{margin}
```{warning}
Web scraping can be very open-ended. Start early so that you have time to get help if you get stuck. 
```
````
The notebook you submit should include:

- a motivating question for why you're combining the datasets in an introduction section
- code and description of how you built and prepared each dataset. For each step,  describe what you're about to do, the code with output, interpretation that leads into the next step.
- exploratory data analysis that shows why you built the data and confirms that is prepared enough to analyze.
- For one pair of tables, show how a different merge could answer a different question.

For construct, this can be very minimal EDA.



The notebook you submit should include:
- a motivating question for why you're combining the datasets in an introduction section
- code and description of how you built and prepared each dataset. For each step describe what you're about to do, the code with output, interpretation that leads into the next step.
- exploratory data analysis that shows why you built the data and confirms that is prepared enough to analyze.

For construct, this can be very minimal EDA.


## Additional achievements

To earn additional achievements, you must do more cleaning and/or exploratory data analysis.


### Prepare level 2
To earn level 2 for prepare, you must manipulate either a component table or the final dataset.  See your Achievement checklist for which aspects of prepare you still need, but sample manipulations include: 

- transform into a tidy format
- add a new column by computing from others
- handle NaN values by dropping or filling
- drop a column, row, or duplicates in another way

### Summarize and Visualize level 2
To earn level 2 for summarize and/or visualize, include additional analyses after building the datasets.

Connect your EDA to questions, and focus on the aspects of these achiements you have not successfully demonstrated. 

### Python Level 2

Use pythonic naming conventions throughout, AND:

- Use pythonic loops and a list or dictionary OR
- use a list or dictionary comprehension

```{admonition} Thinking Ahead
Compare the level 2 skill definitions to level 3, how could you extend and adapt what you've done to meet level 3?
```



```{admonition} Thinking Ahead
You could also demonstrate understanding of how merges work by converting a dataset
that is provided as a single table with redundant information into a number of
smaller tables in a database.
```
