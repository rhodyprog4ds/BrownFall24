---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data Science Achievements

```{code-cell} ipython3
:tags: [remove-input]


import yaml as yml
import pandas as pd
import os
from IPython.display import display, Markdown
pd.set_option('display.max_colwidth', None)


def yml_df(file):
    with open(file, 'r') as f:
        file_unparsed = f.read()

    file_dict = yml.safe_load(file_unparsed)
    return pd.DataFrame(file_dict)

outcomes_df = yml_df('../_data/learning_outcomes.yml')
# outcomes_df.set_index('keyword',inplace=True)
schedule_df = yml_df('../_data/schedule.yml')
schedule_df.set_index('week', inplace=True)
# schedule_df = pd.merge(schedule_df,outcomes_df,right_on='keyword',  left_on= 'clo')
rubric_df = yml_df('../_data/rubric.yml')
rubric_df.set_index('keyword', inplace=True)
```

In this course there are 5 learning outcomes that I expect you to achieve by
the end of the semester.  To get there, you'll focus on 15 smaller achievements
that will be the basis of your grade.  This section will describe how the topics
covered, the learning outcomes, and the achievements are covered over time. In
the next section, you'll see how these achievements turn into grades.


## Learning Outcomes

By the end of the semester


```{code-cell} ipython3
:tags: [remove-input]

outcome_list = [ str(i+1) + '. ' + ' (' + k + ') '  + o  for i,(o,k) in enumerate(zip(outcomes_df['outcome'], outcomes_df['keyword']))]

display(Markdown('  \n'.join(outcome_list)))
#outcomes_df[['keyword','outcome']]
```


We will build your skill in the `process` and `communicate` outcomes over the whole semester. The middle three skills will correspond roughly to the content taught for each of the first three portfolio checks.  

(schedule)=
## Schedule



The course will meet {{ time }} in {{ location }}. Every class will include participatory live coding (instructor types code while explaining, students follow along) instruction and small exercises for you to progress toward level 1 achievements of the new skills introduced in class that day.

Each Assignment will have a deadline posted on the assignment page, typically the same day each week.  Portfolio deadlines will be announced at least 2 weeks in advance.



```{code-cell} ipython3
:tags: [remove-input]


schedule_df.replace({None:'TBD'})
schedule_df[['topics','skills']]
```

(achievement-definitions)=
## Achievement Definitions


The table below describes how your participation, assignments, and portfolios will be assessed to earn each achievement. The keyword for each skill is a short name that will be used to refer to skills throughout the course materials; the full description of the skill is in this table.

```{code-cell} ipython3
:tags: [remove-input]


rubric_df.replace({None:'TBD'},inplace=True)
rubric_df.rename(columns={'mastery':'Level 3',
              'compentent':'Level 2',
              'aware':'Level 1'}, inplace=True)

rubric_df[['skill','Level 1','Level 2','Level 3']]
```


```{code-cell} ipython3
:tags: [remove-input]


assignment_dummies  = pd.get_dummies(rubric_df['assignments'].apply(pd.Series).stack()).groupby(level=0).sum()
assignment_dummies['# Assignments'] = assignment_dummies.sum(axis=1)
col_rename = {float(i):'A' + str(i) for i in range(1,14)}
assignment_dummies.rename(columns =col_rename,inplace=True)

portfolio_dummies  = pd.get_dummies(rubric_df['portfolios'].apply(pd.Series).stack()).groupby(level=0).sum()
col_rename = {float(i):'P' + str(i) for i in range(1,5)}
portfolio_dummies.rename(columns =col_rename,inplace=True)


rubric_df = pd.concat([rubric_df,assignment_dummies, portfolio_dummies],axis=1)

assignment_cols =  ['A'+ str(i) for i in range(1,14)] + ['# Assignments']

portfolio_cols = [ 'Level 3'] + ['P' + str(i) for i in range(1,5)]
```

(assignment-skills)=
### Assignments and Skills

Using the keywords from the table above, this table shows which assignments you will be able to demonstrate which skills and the total number of assignments that assess each skill. This is the number of opportunities you have to earn Level 2 and still preserve 2 chances to earn Level 3 for each skill.

```{code-cell} ipython3
:tags: [remove-input]

rubric_df[assignment_cols]
```

```{warning}
**process** achievements are accumulated a little slower. Prior to portfolio check 1, only level 1 can be earned.  Portfolio check 1 is the first chance to earn level 2 for process, then level 3 can be earned on portfolio check 2 or later.
```

(portfolioskills)=
### Portfolios and Skills

The objective of your portfolio submissions is to earn Level 3 achievements. The following table shows what Level 3 looks like for each skill and identifies which portfolio submissions you can earn that Level 3 in that skill.


```{code-cell} ipython3
:tags: [remove-input]

rubric_df[portfolio_cols]
```

(checklists)=

### Detailed Checklists

```{code-cell} ipython3
:tags: [remove-input]

ach = yml_df('../_data/achievments.yml')

entry = '#### **{name}**\n  \n_{description}_ \n\n{components_checklist}'

def issue_action_str(row):
    rep_dict = {}
    if type(row['components']) ==list:
        rep_dict['components_checklist'] = '\n- [ ] '.join(['']+row['components'])
    else:
        rep_dict['components_checklist'] = ''

    rep_dict['name'] = row['name']
    rep_dict['description'] = row['description']
    return entry.format_map(rep_dict) + '\n'

checklist_list = ach.apply(issue_action_str,axis=1).values
all_checklists = '\n\n'.join(list(checklist_list))

# display(Markdown(all_checklists))
with open('achmd.md','w') as f:
    f.write(all_checklists)
```


```{include} achmd.md
```
