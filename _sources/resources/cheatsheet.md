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

# Cheatsheet

Patterns and examples of how to use common tips in class


## How to use brackets

```{list-table}

* - symbol
  - use
* - `[val]`
  - indexing item val from an object; `val` is int for iterables, or any for mapping
* - `[val : val2]`
  - slicing elemtns val to val2-1 from a listlike object
* - `[ item1,item2 ]`
  - creating a list consisting of `item1` and `item2`
* - `(param)`
  - function calls
* - `(item1,item2)`
  - defining a tuple of `item1` and `item2`
* - `{item1,item2}`
  - defining a set of `item1` and `item2`
* - `{key:val1, key2: val2}`
  - defining a  dictionary where key1 indexes to val2

```


## Axes

```{code-cell} ipython3
:tags: ["remove-input"]

import pandas as pd
```

First build a small dataset that's just enough to display

```{code-cell} ipython3
data = [[1,0],[5,4],[1,4]]
df = pd.DataFrame(data = data,
  columns = ['A','B'])

df
```
This data frame is originally 3 rows, 2 columns.  So summing across rows will give us a {term}`Series` of length 3 (one per row) and long columns will give length 2, (one per column). Setting up our toy dataset to not be a square was important so that we can use it to check which way is which.

```{code-cell} ipython3
df.sum(axis=0)
```

```{code-cell} ipython3
df.sum(axis=1)
```



```{code-cell} ipython3
df.apply(sum,axis=0)
```

```{code-cell} ipython3
df.apply(sum,axis=1)
```

## Indexing

```{code-cell} ipython3
df['A'][1]
```

```{code-cell} ipython3
df.iloc[0][1]
```
