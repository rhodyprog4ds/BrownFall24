# Getting Help with Programming



## Asking Questions

![comic on asking questions, that summarizes blog post](../img/questions.png)

One of my favorite resources that describes how to ask good questions is
[this blog post](https://jvns.ca/blog/good-questions/) by Julia Evans, a developer
who writes comics about the things she learns in the course of her work and
publisher of [wizard zines](https://wizardzines.com/).


## Describing what you have so far

````{margin}
```{note}
A fun version of this is [rubber duck debugging](https://rubberduckdebugging.com/)
```
````

Stackoverflow is a common place for programmers to post and answer questions.  
As such, they have written a good
[guide on creating a minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example).


Creating a minimal reproducible example may even help you debug your own code,
but if it does not, it will definitely make it easier for another person to
understand what you have, what your goal is, and what's working.  

## Understanding Errors

Error messages from the compiler are not always straight forward.  

The {term}`TraceBack` can be a really long list of errors that seem like they are not even
from your code.  It will trace back to all of the places that the error occurred.
It is often about how you called the functions from a library, but the compiler
cannot tell that.

To understand what the traceback is, how to read one, and common examples, see [this post on Real Python](https://realpython.com/python-traceback/#how-do-you-read-a-python-traceback).

One thing to try, is [friendly traceback](https://friendly-traceback.github.io/docs/index.html)
a python package that is designed to make that error message text more clear and
help you figure out what to do next.

`````{admonition} Ram Token Opportunity
If you try out friendly traceback and find it helpful, add a testimonial here. using
````
```{epigraph}
```
````
`````
