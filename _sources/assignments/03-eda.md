
# Assignment 3: Exploratory Data Analysis

**Due:2023-10-01 end of day**



<!-- - [accept assignment](https://classroom.github.com/a/BOG3E7Ch) -->



## Submission
```{important}
You have the option to work with a partner. You must plan this in advance so that you have access to collaborate. 
```
### Solo
Add your work to the assignment3 branch in your portfolio and you do not need to edit the `a3_location` file 

### Group
1. coordinate so that the first person makes the team when they [accept the assigment](https://classroom.github.com/a/caIgkvaR)
2. the second (and third) joins the same team when they [accept the assigment](https://classroom.github.com/a/caIgkvaR). 
3. Each person should [upload their work to a branch ](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository#:~:text=Below%20the%20commit%20message%20fields%2C%20decide%20whether%20to%20add%20your%20commit%20to%20the%20current%20branch%20or%20to%20a%20new%20branch.%20If%20your%20current%20branch%20is%20the%20default%20branch%2C%20you%20should%20choose%20to%20create%20a%20new%20branch%20for%20your%20commit%20and%20then%20create%20a%20pull%20request.) named `d1`, `d2` or `d3` for which dataset checklist you followed from below and open a PR. (each person should do a different dataset)
4. In your portfolio, replace the contents of  the `a3_location.md` file on the assignment3 branch with your team name. We will use that to create a PR to give you your individualized achievements update. 



## Objective & Evaluation

This week your goal is to do a small exploratory data analysis for two datasets (or one if in a group) of your choice.

Eligible skills: (links to checklists)
-  process 1
- access 1 and 2
- summarize 1 and 2
-  visualize 1 



## Related notes

- [](../notes/2024-09-17)
- [](../notes/2024-09-19)



## Choose Datasets

Each Dataset must have at least three variables, but can have more. Both datasets
must have multiple types of variables. These **can** be datasets you used for Assignment 2,
if they meet the criteria below. All datasets must be different datasets even in a group

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

### Dataset 3 (d3)
```{warning}
This is only for groups of 3
```
must include at least:
- two continuous valued variables **and**
- one categorical variable.

## EDA

Use a separate notebook for each dataset, name them `dataset_0x.ipynb` where `x` is the number checklist you are following.

For **each** dataset, in the corresponding notebook complete the following:

1. Load the data to a notebook as a `DataFrame` from url or local path, if local, include the data file in your repository.
2. Write a short description of what the data contains and what it could be used for
3. Explore the dataset in a notebook enough to describe its structure. Use the heading `## Description` and include at least the following with interpretation. *What does the strucutre imply about the conclusions you can draw from this data?  Are there limitations in how to safely interpret the data that the summary helps you see? are the variables what you expect?*

    - shape
    - columns
    - variable types
    - overall summary statisics
4. Ask and answer **at least** 3 questions by using and interpreting statistics and visualizations as appropriate. Include a heading for each question using a markdown cell and H2:`##`. **Make sure your analyses meet the criteria in the check lists below.** Use the checklists to think of what kinds of questions would use those type of analyses and help shape your questions. Your questions can be related or different levels of detail or views on a big picture question as long as the analysis addresses the checklist. 
5. Describe what, if anything might need to be done to clean or prepare this data for further analysis in a finale `## Future analysis` markdown cell in your notebook.


### (overall) Question checklist

be sure that every question (all six, 3 per dataset) has:
- a heading
- at least 1 statistic or plot
- interpretation that answers the question
- the question does not include the name of the statistic or plot in it

````{margin}
```{hint}
Try to think about what each of these requirements translates into, 
as in what methods or constructs is it looking for and use an issue to get early feedback on this (by Monday)
```
````

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


### Dataset 3 Checklist 


```{warning}
This is only for groups of 3
```
make sure that your `dataset_03.ipynb` has:


- overall summary statistics
- two individual summary statistics for one variable
- at least one plot that uses 3 total variables
- a plot and summary table that convey the same information. This can be one statistic or many.


## Peer Review

```{note}
If you work alone and complete 2 analyses you do not need to do this, but you might review these
questions because they are similar to how we will grade. 
```

With a partner (or group of 3 where person 1 review's 2 work, 2 reviews 3, and 3 reviews 1) read
your partner's notebook and complete a peer review on their pull request.  You can do peer review
when you have done most of your analysis, and explanation, even if some parts of the code do not
work.

You will complete your review on a PR, by reviewing it.  If you want a big picture overview on that, the [github PR review "course"](https://github.com/skills/review-pull-requests) is a good place to go, it is designed to take <30 minutes. 

1. [start a review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#starting-a-review)
2. (optional) Use [PR comments](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request) to denote places that are confusing or if you see solutions to problems your classmate could not solve *this is hard on notebook files, so it is okay to skip*
1. Prepare to [submit your review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review)
1.  Use the list of questions below for your summary review (copy the template into the box and fill in )

````{important}
Your review should use the **template** for organization, but the **questions** guide what sorts of 
aspects to consider across the sections.  
````

### Review Questions


1. Describe overall how it was to read the analysis overall to read. Was it easy? hard? cohesive? jumpy?
2. How did the data summaries help prepare you to read the rest of the analysis? What do you think might be missing?
3. For each question, consider the following and write any tips for improvement 
   1. Does the question make sense based on the data? How does it relate to the real world is there a reasonable audience? How could the question be improved
   2. How well do the statistics and plots match the question?
   3. Are the interpretations complete, clear, and consistent with the statistics and plots?
   4. What could be done to make the explanations more clear and complete?
   5. What additional analysis might make the analysis more compelling and clear?

#### Template
```
## Overall 
 <!-- Describe overall how it was to read the analysis overall to read. Was it easy? hard? cohesive? jumpy? -->


## Intro

## Question 1 

## Question 2

## Question 3 
```


### Response

Respond to the review on your notebook either with inline comments, replies, or by updating your analysis accordingly.


## Tips and Hints

- Remember you can also use [masking](masking) in your EDA even though we did not do any in class
- To ensure you understand the checklist you can **optionally** make an issue using the appropriate issue type from your repo   and fill in what it should be to get early feedback that you are on track 
- variable types are in the notes
- the [DataFrame](https://pandas.pydata.org/docs/reference/frame.html) API reference shows all the methods (and more) grouped by high level concepts. 



## Think Ahead
````{margin}
```{warning}
This section is not required, but is intended to help you get started thinking
about ideas for your portfolio.  If you complete it, we'll give your feedback to
help shape your ideas to get to level 3 achievements.  If you want to focus only
on level 2 at this moment in time, feel free to skip this part.
```
````

This can be addded to any or all of the datasets

```markdown

## Thinking Ahead 
1. How could you make more customized summary tables?
1. Could you use any of the variables in this dataset to add more variables that would make interesting ways to apply split-apply-combine? (eg thresholding a continuous value to make a categorical value or like what we did with `commodity` in class)
1. Are there multiple ways to answer your big picture question (like different thresholding or subsets of the data)
1. Could any cleaning improve your analyis? 
```
