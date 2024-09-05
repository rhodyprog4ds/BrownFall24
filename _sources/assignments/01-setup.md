
# Assignment 1: Setup, Syllabus, and Review

__Due: 2024-09-10 2:00pm__ 

```{warning}
This is a draft, and will get updated and you will get a notification. 

Mainly submission details will be added
```

## Evaluation 
Eligible skills: (links to checklists)
- Python
- Process

## Related notes
```{warning}
the links below will not work until the relevant notes are posted, after class
```

<!-- - [](../notes/2023-09-07) -->
  
## Instructions

<!-- ````{margin}
```{note}
After accepting the assignment and creating a repository, create an issue on your repository, describing what you're stuck on and tag us with `@rhodyprog4ds/instructors`.

To do this click Issues at the top, the green "New Issue" button and then type away.
```
```` 
-->

```{important}
If you have trouble, check the GitHub FAQ on the left first
````

Your task is to:
1. Install required software from the Tools & Resource page (should have been done before the first class)
2. Create your portfolio, (instructions will be updated and a notification posted)
3. Learn about your portfolio from the README file on your repository.
4. Follow instructions in the README to make your portfolio your own with information about yourself(completeness only) and your own definition of data science (graded for **level 1 process**)
5. complete the `success.md` file as per the instructions in the comments in that file (it is a syllabus quiz)
6. Create a Jupyter notebook called `grading.ipynb` and write a function that computes a grade for this course, with the  docstring below. Your notebook will need to be organized and readable in a data science style, following style from other courses will not earn credit. 
7. (additional programming step to assess prerequisite knowledge, tba)
<!-- 
1. [Upload the notebook to your repo](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) directly on the main branch. 
2. Add the line `  - file: grading` in your `_toc.yml` file. 


the syntax of the line added to your `_toc.yml` has to be exact


-->

<!-- ```{warning}
Do not merge your "Feedback" Pull Request
````
 -->

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
 - markdown cells with explanation of the calls and anything else so that the notebook reads like a report. 



