
# Assignment 2: Practicing Python and Accessing Data

Quick Facts
- due : 2023-09-18
- [accept assignment](https://classroom.github.com/a/BOG3E7Ch)


## Objective & Evaluation
This assignment is an opportunity to earn level 1 and 2 achievements in `python` and `access` and begin working toward level 1 for `summarize`. You can also earn level 1 for `process`.

Eligible skills: (links to checklists)
- **first chance** access [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#access-level2)
- python [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level1) and [2](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#python-level2)
- summarize [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#summarize-level1) 
- process [1](https://rhodyprog4ds.github.io/BrownFall22/syllabus/achievements.html#process-level1) 

This assignment is an opportunity to earn level 1 and 2 achievements in `python` and `access` and begin working toward level 1 for `summarize`. You can also earn level 1 for `process`.

In this assignment, you'll practice/ review python skills by manipulating datasets
and extracting basic information about them.

## Related notes

- [](../notes/2023-09-12)
- [](../notes/2023-09-14)


## Setting

Next week, we are going to learn about summarizing data. In this assignment, you are going to build a small dataset about datasets. In class next week, we will combine all of your datasets about datasets together in order to be able to answer questions like:

- how much total data did you all load
- how many students picked the same dataset?
- how many total rows of data did each student load?


## Find Datasets

Find 3 datasets of interest to you that are provided in at least two different file formats. Choose datasets that are not too big, so that they do not take more than a few second to load. At least one dataset, must have non numerical (eg string or boolean) data in at least 1 column.

In your notebook, create a markdown cell for each dataset that includes:
- heading of the dataset's name
- a 1-2 sentence summary of what the dataset contains and why it was collected
- a "more info" link to where someone can learn about the dataset
- 1-2 questions you would like to answer with that dataset.

## Store info about data for loading

Create a list of dictionaries in `datasets.py`, so that there is one dictionary for each dataset. Each dictionary should have the following keys:

```{list-table} Meta data of the dictionaries
:header-rows: 0

* - `url`
  - the full url of the dataset
* - `short_name`
  - a short name
* - `load_function`
  - (the actual function handle) what function should be used to load the data into a `pandas.DataFrame`.

```

```{hint}
See below for how you will use the dictionary as help for how you should construct it
```

## Make a dataset about your datasets

````{margin}
```{hint}
See they [python module docs for examples](https://docs.python.org/3/tutorial/modules.html#modules)
```
````
In a notebook called `dataset_of_datasets.ipynb`, import the list of dictionaries from the `datasets` module you created in the step above. 
Then {term}`iterate` over the list of dictionaries, and:  

1. load each dataset like `dataset_dict['load_function'](dataset_dict['url'])`
1. save it to a local csv using the short name you provided for the dataset as the file name, without writing the index column to the file.
1. record attributes about the dataset as in the table below in a list or dictionary  of lists 
1. Use that to create a DataFrame with columns that match the rows of the following table.

```{list-table} Meta Data Description of the DataFrame to build
:header-rows: 0

* - name
  - a short name for the dataset
* - source
  - a url to where you found the data
* - num_rows
  - number of rows in the dataset
* - num_columns
  - number of columns in the dataset
* - num_numerical
  - number of numerical variables in the dataset
```

## Explore Your Datasets

In a second notebook file called `exploration.ipynb`: 

For one dataset that includes nonnumerical data:
- read it in from your local csv using a relative path
- display the heading and the first 6 rows
- make a numpy array of only the numerical data and save it to a new variable (select these programmatically)
- was the format that the data was provided in a good format? why or why not?


For any other dataset:
- read it in from your local csv using a relative path
- display the heading with the last seven rows
- display the datatype for each column
- Are there any variables where pandas may have read in the data as a datatype that's not what you expect (eg a numerical column mistaken for strings)? If so, investigate and try to figure out why.

For the third dataset:
- read it in from your local csv  using a relative path
- save every fifth row (5,10,15 ,...) of the data for two columns of your choice into a new DataFrame and display that

## Exploring data files

There are two files in the data folder, both can be read in with `read_csv` but need some options or fixing.

- try to read in the `german.data` file, what happens with the default settings? What option do you need to use to make it look right?
- try to read in the `.csv` file that's included in the template repository (), use the error messages you get to try to fix the file manually (any text editor, including jupyter can edit a `.csv`), making notes about what changes you made in a markdown cell.



## Submission

This time you have to separately submit from posting your code to make grading easier.  

1. Go to the actions tab 
2. Click the action called "Prepare & Submit" in the left hand sidebar
3. click the run workflow button on the right hand side.
4. Cilck run workflow

```{hint}
see the [github docs](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow) for screenshots of how to do these steps. 
```

## Thinking ahead

```{important}
This section is not required, but is intended to help you get started thinking
about ideas for your portfolio.  If you complete it, we'll give your feedback to
help shape your ideas to get to level 3 achievements.  If you want to focus only
on level 2 at this moment in time, feel free to skip this part. You could also think about these after submitting the assignment. If you want, you could discuss these ideas in office hours.
```


1. When might you prefer one datatype over another?
1. How does PEP 8 standard code help you be collaborative?
1. Learn about [Datasheets for Datasets](https://arxiv.org/pdf/1803.09010.pdf) and find some examples, (eg this [google scholar result](https://scholar.google.com/scholar?q=datasheets+for+datasets&hl=en&as_sdt=0&as_vis=1&oi=scholart) ) How could something like this impact your work as a data scientist?
