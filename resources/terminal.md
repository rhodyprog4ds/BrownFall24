# Terminals and Environments


## Why all this work?

Managing environments is **one of the hardest parts of programming** so, as instructors,
we often design our courses around not having to do it.  In this class, however,
I'm choosing to take the risk and help you all through beginning to manage your
own environments.  
````{margin}
```{note}
We know that we don't currently teach a lot of this in our department, so in
Spring 22 I'm teaching a brand new course on Computer Systems, that will help
you understand the underlying concepts that make all of this stuff make sense,
instead of just following recipes and debugging here and there.
```
````

These issues will be the most painful in the course, I promise.

I think it's worth this type of pain though, because all fo the code you ever
run must run in *some* sort of environment.  By giving you control, I'm hoping
to increase your indepence as a programmer.  This also means responsibility and
some messy debugging, but I think this is a good tradeoff.  This is an upper
level (300+) level course, so increasing some complexity is expected and I want
as much as possible to keep you close to realisitc programming environments; so
that what you see in this course is **directly, and immediately,** applicable in
real world contexts.  You should be able to pick up data science side projects
or an internship with ease after this course.  


I *know* some of these things will be frustrating at times, but I want you to
feel supported in that and know that your grade will not be blocked by you
having environment issues, as long as you ask for help in a timely matter.  

```{margin}
If, for example, you come to me in week 5 and have never got an any environment
working and you're trying for the first time, your grade will be hurt because
you will be very far behind at that point.
Ask for help early and often.
```


## Windows

Windows has a sort of multiverse of terminal environments.

The least setup required involves using anaconda prompt and `conda` to manage
you python environment and GitBash to work with git (and it can also do other
bash related things).

Instead of managing two terminals, you may [configure your path in GitBash to
make Anaconda work](https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found)

## MacOS

MacOS has one terminal app, but it can run different shells.

On MacOS You may want to switch to bash (using the `bash` command or make it your default and [update bash](https://itnext.io/upgrading-bash-on-macos-7138bd1066ba).
