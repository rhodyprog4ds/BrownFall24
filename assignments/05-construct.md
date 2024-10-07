# Assignment 5: Constructing Datasets and Using Databases

<!-- {{ accept_assignment }} -->



due date : 2023-10-10

Skills:
- prepare level 1
- summarize 1,2
- visualize 1,2
- python 1,2


## Related notes

- [Webscraping](https://rhodyprog4ds.github.io/BrownFall24/notes/2024-10-01.html)
- [Merging Data & Databases](https://rhodyprog4ds.github.io/BrownFall24/notes/2024-10-03.html)


## Constructing Datasets


Your goal is to programmatically construct a ready to analyze dataset that combines information from multiple sources. This can be in a crawing fashion like we did for the CS people or by combining two tables with a merge. If you use a merge to meet the multiple sources criterion, only one source must be scraped, the second can be provided as tabular data.  


````{margin}
```{warning}
Web scraping can be very open-ended. Start early so that you have time to get help if you get stuck. 
```
````
The notebook you submit should include:

- a motivating question for why your are building the dataset you are building
- code and description of how you built and prepared your dataset. For each step,  describe what you're about to do, the code with output, interpretation that leads into the next step.
- exploratory data analysis that shows why you built the data and confirms that is prepared enough to analyze. 
- also save your dataset to csv


For construct only, this can be very minimal EDA.



## Additional achievements

To earn additional achievements, you must do more cleaning and/or exploratory data analysis.


### Prepare level 2
To earn level 2 for prepare, you must manipulate either a component table or the final dataset. Sample manipulations include: 

- transform into a tidy format
- add a new column by computing from others
- handle NaN values by dropping or filling
- drop a column, row, or duplicates in another way
- change a continuous value to categorical (there is an added section in the notes on [quantizing](quantize) that we did not do in class, but should be easy to follow)


### Summarize and Visualize level 2
To earn level 2 for summarize and/or visualize, include additional analyses after building the datasets.

Connect your EDA to questions, and demonstrate demonstrate items from one of the checklists in A3. 

### Python Level 2

Use pythonic naming conventions throughout, AND:

- Use pythonic loops and a list or dictionary OR
- use a list or dictionary comprehension

this can be in your cleanup or your EDA

```{admonition} Thinking Ahead
Compare the level 2 skill definitions to level 3, how could you extend and adapt what you've done to meet level 3?
```



```{admonition} Thinking Ahead
You could also demonstrate understanding of how merges work by converting a dataset
that is provided as a single table with redundant information into a number of
smaller tables in a database.
```
