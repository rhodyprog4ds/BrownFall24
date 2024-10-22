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
# Deepening your knowledge

Completing the basic assignments that demonstrate you can apply what we cover in class to your own data, is enough for a B, to earn an A you need to extend your knowledge. 

You have some different pathways to earning an A.  

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

## Extending Assignments


Starting in week 3 it is recommended that you spend some time each week working on extensions to earn level 3 on the skills.

Use the feedback you get on assignments to inspire your extensions.

To submit these, submit the work to a separate `<assignment>extended` branch so for assignment 2 extension, submit to `assignment2extended`.

You should **not** extend *every* assignment since skills overlap and relate to one another. 

I recommend making an issue that is a plan and asking for feedback before you work on extensions, so that you do not do too much extra work. 

Some ideas:
- extend A5 to add in a database source or combine the data in new ways, plus do extended EDA to earn level 3 for: access, construct, prepare, visualize and summarize
- extend one of A7-9 to have experiments that more carefully analyze and compare different models at a task for one of the ml tasks (classification, regression, clustering) and visualize and summarize

## Deployment and Distribution

```{warning}
this is currently a draft, will be updated by 10/24
```

Instead of earning all 15 level 3s you can earn any 10 plus the following: 
- transform your portfolio to a publish-able portfolio by making it a jupyter book (mostly set up already, just need to clean up)
- share a model and use a classmate's model with [huggingface](https://huggingface.co/CSC310-fall24) (making the model card would count for process and fitting it could count for one of the 3 tasks)

if you go this route, I recommend level 3 for: 
- access (loading models from huggingface will count)
- python 
- process (see [](process.md))
- summarize
- visualize
- evaluate
- one of: classification, regression, clustering
- optimize
- compare
- workflow

If your dataset of interest is hard to work with, images, or text, you might swap in 
representation instead of access

this means skipping level 3 for:
- prepare
- construct
- 2 of:  classification, regression, clustering
- representation