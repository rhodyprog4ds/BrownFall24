---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(portolioindex)=
# Portfolio

```{code-cell} ipython3
:tags: [remove-input]


import yaml as yml
import pandas as pd
import os
pd.set_option('display.max_colwidth', None)


def yml_df(file):
    with open(file, 'r') as f:
        file_unparsed = f.read()

    file_dict = yml.safe_load(file_unparsed)
    return pd.DataFrame(file_dict)

outcomes_df = yml_df('../_data/learning_outcomes.yml')
outcomes_df.set_index('keyword',inplace=True)
schedule_df = yml_df('../_data/schedule.yml')
schedule_df.set_index('week', inplace=True)
# schedule_df = pd.merge(schedule_df,outcomes_df,right_on='keyword',  left_on= 'clo')
rubric_df = yml_df('../_data/rubric.yml')
rubric_df.set_index('keyword', inplace=True)
rubric_df.replace({None:'TBD'},inplace=True)
rubric_df.rename(columns={'mastery':'Level 3',
              'compentent':'Level 2',
              'aware':'Level 1'}, inplace=True)

assignment_dummies  = pd.get_dummies(rubric_df['assignments'].apply(pd.Series).stack()).groupby(level=0).sum()
assignment_dummies['# Assignments'] = assignment_dummies.sum(axis=1)
col_rename = {float(i):'A' + str(i) for i in range(1,14)}
assignment_dummies.rename(columns =col_rename,inplace=True)

portfolio_dummies  = pd.get_dummies(rubric_df['portfolios'].apply(pd.Series).stack()).groupby(level=0).sum()
col_rename = {float(i):'P' + str(i) for i in range(1,5)}
portfolio_dummies.rename(columns =col_rename,inplace=True)


rubric_df = pd.concat([rubric_df,
                      assignment_dummies,
                      portfolio_dummies],axis=1)

assignment_cols =  ['A'+ str(i) for i in range(1,14)] + ['# Assignments']

portfolio_cols = [ 'Level 3'] + ['P' + str(i) for i in range(1,5)]
portfolio_df = rubric_df[portfolio_cols]
```

This section of the site has a set of portfolio prompts and this page has instructions for portfolio submissions.  

Starting in week 3 it is recommended that you spend some time each week working on items for your portfolio, that way when it's time to submit you only have a little bit to add before submission.

The portfolio is your only chance to earn Level 3 achievements, however, if you have not earned a level 2 for any of the skills in a given check, you could earn level 2 then instead.
The prompts provide a starting point, but remember that to earn achievements, you'll be evaluated by the rubric.
You can see the full rubric for all portfolios in the [syllabus](portfolioskills).
Your portfolio is also an opportunity to be creative, explore things, and answer your own questions that we haven't answered in class to dig deeper on the topics we're covering.
Use the feedback you get on assignments to inspire your portfolio.

Each submission should include an introduction and a number of 'chapters'.  The grade will be based on both that you demonstrate skills through your chapters that are inspired by the prompts and that your summary demonstrates that you *know* you learned the skills. See the [formatting tips](formatting) for advice on how to structure files.


On each chapter(for a file) of your portfolio, you should identify which skills by their keyword, you are applying.

You can view a (fake) example [in this repository](https://github.com/rhodyprog4ds/portfolio-brownsarahm) as a [pdf](https://github.com/rhodyprog4ds/portfolio-brownsarahm/blob/gh-pages/portfolio.pdf) or as a [rendered website](https://rhodyprog4ds.github.io/portfolio-brownsarahm/intro.html)

## Upcoming Checks

<!-- ### Portfolio 1 -->
- Portfolio Check 1 is due 
<!-- - Portfolio Check 2 is due 
- Portfolio check 3 is due 
- Portfolio check 4 is due  -->




Portfolio check 2 will assess the following *new* achievements in addition to an a chance to make up any that you have missed:

```{code-cell} ipython3
:tags: [remove-input]

portfolio_df['Level 3'][portfolio_df['P2']==1].reset_index().set_index('keyword')
```

<!--

```{important}
start early, assignment 9 and 10 will be due on Wednesdays like regular the week before and of this deadline. You will get feedback on Assignment 9 by Friday so that you can use that to update your portfolio on the construct achievements.
```

The third submission will be graded on the following criteria and due on December 4:

```{code-cell} ipython3
:tags: [remove-input]

portfolio_df['Level 3'][portfolio_df['P3']==1].reset_index().set_index('keyword')
```


```{code-cell} ipython3
:tags: [remove-input]

portfolio_df['Level 3'][portfolio_df['P4']==1].reset_index().set_index('keyword')
```
 -->

```{code-cell} ipython3

```
