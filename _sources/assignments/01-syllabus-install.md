---
substitutions:
  accept_assignment: |
    [accepting the assignment](https://classroom.github.com/a/oIJowjlW)
  date : 2023-09-11
---

# Assignment 1: Setup, Syllabus, and Review

__Due: 2023-09-11__


## Evaluation 
Eligible skills: (links to checklists)
- {fa}`star`[^starredskill]  python [level 1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#python-level1) and [level 2](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#python-level2)
- {fa}`star`process[^processnote] [level 1](https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html#process-level1) 

[^starredskill]: skills will be marked like this on the first time they are eligible. There will also be a {fa}`hourglass-end`  on skills for the last assignment they are eligible
[^processnote]: process is a special skill. You'll earn level 1 in this assignment or a soon one and level two in either portfolio 1 or assignments 6-10, then level 3 in portfolio 2,3, or 4. 

## Related notes
```{warning}
the links below will not work until the relevant notes are posted, after class
```

- [](../notes/2023-09-07)
  
## Instructions

````{margin}
```{note}
After accepting the assignment and creating a repository, create an issue on your repository, describing what you're stuck on and tag us with `@rhodyprog4ds/instructors`.

To do this click Issues at the top, the green "New Issue" button and then type away.
```
````

```{important}
If you have trouble, check the GitHub FAQ on the left first
````

Your task is to:
1. Install required software from the Tools & Resource page (should have been done before the first class)
1. Create your portfolio, by [accepting the assignment](https://classroom.github.com/a/5YFy9MQZ)
1. Learn about your portfolio from the README file on your repository.
1. Follow instructions in the README to make your portfolio your own with information about yourself(not evaluated, but useful) and your own definition of data science (graded for **level 1 process**)
2. complete the `success.md`` file as per the instructions in the comments
3. Create a Jupyter notebook called `grading.ipynb` and write a function that computes a grade for this course, with the  docstring below.
4. [Upload the notebook to your repo](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) directly on the main branch. 
5. Add the line `  - file: grading` in your `_toc.yml` file.

```{important}
the syntax of the line added to your `_toc.yml` has to be exact
```

```{warning}
Do not merge your "Feedback" Pull Request
````

### Docstring

```
    '''
    Computes a grade for CSC/DSP310 from numbers of achievements at each level

    Parameters:
    ------------
    num_level1 : int
      number of level 1 achievements earned
    num_level2 : int
      number of level 2 achievements earned
    num_level3 : int
      number of level 3 achievements earned

    Returns:
    --------
    letter_grade : string
      letter grade with possible modifier (+/-)
    '''

```

### Sample tests 

Here are some sample tests you could run to confirm that your function works correctly:
````{margin}
```{warning}
remember the difference between side effects and returns
```


```{note}
when the value of the expression after `assert` is `True`, it will look like nothing happened. `assert` is used for testing
```
````

```
assert compute_grade(15,15,15) == 'A'

assert compute_grade(15,15,13) == 'A-'

assert compute_grade(15,14,14) == 'B-'

assert compute_grade(14,14,14) == 'C-'

assert compute_grade(4,3,1) == 'D'

assert compute_grade(15,15,6) =='B+'
```

### Notebook Checklist 

 -  a Markdown cell with a heading
 - your function called `compute_grade`
 - three calls to your function that verify it returns the correct value for different number of badges that produce at three different letter grades.

### Grading Notes: 

 - a basic function that uses conditionals in python will earn **level 1 python**
 - to earn **level 2 python** use pythonic code to write a loop that tests your function's correctness, by iterating over a list or dictionary. Remember you will have many chances to earn level 2 achievement in python, so you do not need to do this step for this assignment if you are not sure how. 


