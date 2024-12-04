
# Assignment 11: Fake News

## Quick Facts
- [accept the assignment](https://classroom.github.com/a/D1fjut40)
- __first: 2024-12-04__
- __final: 2024-12-11__



```{note}
there are 2 deadlines for this instead of an assignment 12. This means that we will review whatever you have done by the 12/4 on 12/5-6 and then give you personalized feedback in order to finish the assignment or extend it.  
```
<!-- - First feedback: {{ early }}
__Final due date: {{ date }}__ -->


## Related notes

- [Intro to NLP](https://rhodyprog4ds.github.io/BrownFall24/notes/2024-11-19.html)
- [Classifying Text](https://rhodyprog4ds.github.io/BrownFall24/notes/2024-11-21.html)
- [Breaking Down a problem](https://rhodyprog4ds.github.io/BrownFall24/notes/2024-11-26.html)
<!-- - [more text representations](../notes/2023-11-28) -->

## Assessment

Eligible skills: (links to checklists)
- representation 1,2
- workflow 1,2
- summarize 1,2
- visualize 1,2
- compare 1,2
- optimize 1,2
- classifciation 1,2
- regression 1,2
- clustering 1,2


## Instructions

Use the dataset in the assignment template repo to answer the following questions:

1. Is the text or the title of an article more predictive of whether it is real or fake?
1. Are titles of real or fake news more similar to one another?

The data includes variables:
- ‘text’: contents of an article
- ‘label’: whether it is real or fake news
- 'title': title of the article


::::{margin}
:::{tip}
Tuesday November 26 will be a problem solving session where we will discuss how to break this problem down.  You should be able to leave class with an approved outline tht will set you up to complete the assignment.  I will also provide help in planning for which achievements you want to target. 
:::
::::

Include narrative around the code required to answer these and interpret the results to give an actual answer. 
- Provide context on your answer and consider how strong it is based on what differences you can have in how you represent the data and how that might impact your model performance. 
- Consider if the analysis you have done is enough evidence answer the question from the analysis you have completed or could something else change the answer. 
- Use summary statistics and visualizations appropriately in order to explain your results.
- To earn compare, you can compare classifiers or representations, but make sure it is an appriate comparison
- If you have questions about how to work on any specific achievement post an issue on the repo


```{hint}
The data set contains a large number of articles (takes a long time to train), you can downsample this to something like a 1,000 articles or so in order to speed up training and evaluation (hint: use sample).

```

## Extension ideas

:::{note}
For each of these you need to show, in your report, *why* this works with evidence based on your data analysis. If you do steps outside the notebook (eg prompting an llm) you need to include, in a markdown cell, a detailed explanation of what you did, for example:
> I used LLMX to generate Y new articles, using the PROMPT and ...
:::

- stress test your model by generating additional fake news using an LLM and scraping additional, newer, high quality news articles(if possible, some news agencies are mad at LLM training procedures and have locked their content down) or using the ones in the 20 news groups dataset
- based on your analysis how could you help teach a person to spot fake news? (hint: model inspection)
- How could you get an llm to generate news articles that your classifier thinks are real? (hint: model inspection)
- how does it work if you use both the text and the title? Could you give people a simple flowchart that guides them to scan the title for things and then the article? How reliable can that be? 


```{tip}
If you like stress-testing models, there is a new course in spring 2025: CSC 492 - Machine Learning Security and Privacy.  Dr. Kaleel Mahmood will be the instructor.  The prerequisites for the course are:

- MATH 215 or an equivalent background in linear algebra **and** 
- CSC 310 or an equivalent knowledge of Python programming

If you would like to enroll in this class, or have questions about it, contact [Dr. Mahmood](https://web.uri.edu/cs/meet/kaleel-mahmood/).

He will also offer an LLM course in Fall 2025 (I think only at 500 level, but possibly at both 400/400). 

If you like trying to figure out what models do in greater detail and why, I am teaching [Model Evaluation and Explanation](https://evalexplainai.github.io/) as CSC592 in spring 2025. 
```
