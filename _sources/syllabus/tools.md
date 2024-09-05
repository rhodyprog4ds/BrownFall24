# Tools and Resources

We will use a variety of tools to conduct class and to facilitate your programming. You will need a computer with Linux, MacOS, or Windows. It is unlikely that a tablet will be able to do all of the things required in this course. A Chromebook may work, especially with developer tools turned on. Ask Dr. Brown if you need help getting access to an adequate computer.


All of the tools and resources below are either:

  - paid for by URI **OR**
  - freely available online.



````{margin}
```{important}

TL;DR [^tldr]

  - check Brightspace
  - Log in to Prismia Chat
  - Make a GitHub Account
  - Install Python
  - Install Git
```
````

## BrightSpace

````{margin}
```{note}
Seeing the BrightSpace site requires loging in with your URI SSO and being enrolled in the course
```
````
This will be the central location from which you can access links to other materials.
Any links that are for private discussion among those enrolled in the course will be available only from our course [Brightspace site](https://brightspace.uri.edu/d2l/home/226416).

<!-- 
For announcements, you can [customize](https://documentation.brightspace.com/EN/le/announcements/learner/enable_notifications_in_announcements.htm) how you receive them. -->


## Prismia chat

Our class link for [Prismia chat](https://prismia.chat/) is available on Brightspace.
We will use this for chatting and in-class understanding checks.

On Prismia, all students see the instructor's messages, but only the Instructor and TA see student responses. 

## Course website

The course manual will have content including the class policies, scheduling, class notes, assignment information, and additional resources.
This will be linked from Brightspace and available publicly online at [rhodyprog4ds.github.io/BrownSpring23/](https://rhodyprog4ds.github.io/BrownSpring23/).
Links to the course reference text and code documentation will also be included here in the assignments and class notes.

## GitHub

You will need a [GitHub](https://github.com/) Account. If you do not already have one, please [create one](https://github.com/signup) by the first day of class. If you have one, but have not used it recently, you may need to update your password and login credentials as the [Authentication rules](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/about-authentication-to-github) changed over the summer.  In order to use the command line with https, you will need to us the [GitHub CLI](https://cli.github.com/) or  [create a Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) for each device you use. In order to use the command line with SSH, set up your public key.



(prorgramming-env)=
## Programming Environment

This a programming course, so you will need a programming environment. In order to complete assignments you need the items listed in the requirements list. The easiest way to meet these requirements is to follow the recommendations below. I will provide instruction assuming that you have followed the recommendations.

#### Requirements:
- Python with scientific computing packages (numpy, scipy, jupyter, pandas, seaborn, sklearn)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- A web browser compatible with [Jupyter Notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html#step-0-the-browser)
<!-- - Openrefine -->

````{margin}
```{note}
all Git instructions will be given as instructions for the command line interface and GitHub specific instructions via the web interface. You may choose to use GitHub desktop or built in IDE tools, but the instructional team may not be able to help.
```
````

```{warning}
Everything in this class will be tested with the up to date (or otherwise specified) version of Jupyter Notebooks. Google Colab is similar, but not the same, and some things may not work there. It is an okay backup, but should not be your primary work environment.
```

#### Recommendation:
- Install python via [Anaconda](https://www.anaconda.com/products/individual)
- if you use Windows, install Git with [GitBash](https://gitforwindows.org/) ([video instructions](https://youtu.be/339AEqk9c-8)).
- if you use MacOS, install Git with the Xcode Command Line Tools. On Mavericks (10.9) or above you can do this by trying to run git from the Terminal the very first time.`git --version`
- if you use Chrome OS, follow these instructions:
1. Find Linux (Beta) in your settings and turn that on.
2. Once the download finishes a Linux terminal will open, then enter the commands: sudo
apt-get update and sudo apt-get upgrade. These commands will ensure you are up to
date.
3. Install tmux with:

    ```
    sudo apt -t stretch-backports install tmux
    ```
4. Next you will install nodejs, to do this, use the following commands:

    ```
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash
    sudo apt-get install -y nodejs
    sudo apt-get install -y build-essential.
    ```
5. Next install Anaconda’s Python from the website provided by the instructor and use the
top download link under the Linux options.
6. You will then see a .sh file in your downloads, move this into your Linux files.
7. Make sure you are in your home directory (something like home/YOURUSERNAME),
do this by using the `pwd` command.
8. Use the `bash` command followed by the file name of the installer you just downloaded to
start the installation.
9. Next you will add Anaconda to your Linux PATH, do this by using the `vim .bashrc`
command to enter the .bashrc file, then add the `export
PATH=/home/YOURUSERNAME/anaconda3/bin/:$PATH` line. This can be placed at the
end of the file.
10. Once that is inserted you may close and save the file, to do this hold escape and type `:x`,
then press enter. After doing that you will be returned to the terminal where you will then
type the source .bashrc command.
11. Next, use the `jupyter notebook –generate-config` command to generate a Jupyter
Notebook.
12. Then just type `jupyter lab` and a Jupyter Notebook should open up.

(texteditor)=
Optional:

- Text Editor: you may want a text editor outside of the Jupyter environment. Jupyter can edit markdown files (that you'll need for your portfolio), in browser, but it is more common to use a text editor like Atom or Sublime for this purpose.


Video install instructions for Anaconda:
- [Windows](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)
- [Mac](https://www.youtube.com/watch?v=TcSAln46u9U)

On Mac,  to install python via environment, [this article may be helpful](https://opensource.com/article/19/5/python-3-default-mac)
- I don't have a video for linux, but it's a little more straight forward.

### Textbook

The text for this class is a reference book and will not be a source of assignments. It will be a helpful reference and you may be directed there for answers to questions or alternate explanations ot topics.

Python for Data Science is available free [online](https://jakevdp.github.io/PythonDataScienceHandbook/):





### Zoom (backup and office hours only)

[^tldr]: Too long; didn't read.

This is where we will meet if for any reason we cannot be in person. You will find the link to class zoom sessions on Brightspace.

URI provides all faculty, staff, and students with a paid Zoom account. It *can* run in your browser or on a mobile device, but you will be able to participate in class best if you download the [Zoom client](https://zoom.us/download) on your computer. Please [log in](https://uri-edu.zoom.us/) and [configure your account](https://uri-edu.zoom.us/profile).  Please add a photo of yourself to your account so that we can still see your likeness in some form when your camera is off. You may also wish to use a virtual background and you are welcome to do so.  

Class will be interactive, so if you cannot be in a quiet place at class time, headphones with a built in microphone are strongly recommended.

For help, you can access the [instructions provided by IT](https://web.uri.edu/itservicedesk/zoom-at-uri/).
