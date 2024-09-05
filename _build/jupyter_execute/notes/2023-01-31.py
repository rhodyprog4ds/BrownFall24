#!/usr/bin/env python
# coding: utf-8

# # Grading review, Pandas, and Iterables
# 
# 
# ## Grading Calculation 
# 
# here is my solution

# In[1]:


def compute_grade(num_level1,num_level2,num_level3):
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
      letter grade with modifier (+/-)
    '''
    if num_level1 == 15:
        if num_level2 == 15:
            if num_level3 == 15:
                grade = 'A'
            elif num_level3 >= 10:
                grade = 'A-'
            elif num_level3 >=5:
                grade = 'B+'
            else:
                grade = 'B'
        elif num_level2 >=10:
            grade = 'B-'
        elif num_level2 >=5:
            grade = 'C+'
        else:
            grade = 'C'
    elif num_level1 >= 10:
        grade = 'C-'
    elif num_level1 >= 5:
        grade = 'D+'
    elif num_level1 >=3:
        grade = 'D'
    else:
        grade = 'F'


    return grade


# Note that we can verify it works using `assert`

# In[2]:


assert compute_grade(15,15,15) =='A'


# In[3]:


assert compute_grade(15,15,9) =='B+'


# this also means we can assign the value out

# In[4]:


my_grade = compute_grade(15,11,5)


# In[5]:


my_grade


# Alternatively if we use a side effect instead, printing the value instead of returning it.

# In[6]:


def compute_grade_sideeffect(num_level1,num_level2,num_level3):
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
      letter grade with modifier (+/-)
    '''
    if num_level1 == 15:
        if num_level2 == 15:
            if num_level3 == 15:
                grade = 'A'
            elif num_level3 >= 10:
                grade = 'A-'
            elif num_level3 >=5:
                grade = 'B+'
            else:
                grade = 'B'
        elif num_level2 >=10:
            grade = 'B-'
        elif num_level2 >=5:
            grade = 'C+'
        else:
            grade = 'C'
    elif num_level1 >= 10:
        grade = 'C-'
    elif num_level1 >= 5:
        grade = 'D+'
    elif num_level1 >=3:
        grade = 'D'
    else:
        grade = 'F'


    print( grade)


# Look this way it looks similar:

# In[7]:


compute_grade_sideeffect(15,15,15)


# In[8]:


compute_grade(15,15,15)


# and python lets us assign something

# In[9]:


my_grade = compute_grade_sideeffect(15,15,15)


# but the output is nothing

# In[10]:


type(my_grade)


# ## Loading data with Pandas
# 
# First we learned about the dataset then we can load it.

# In[11]:


coffee_data_url = 'https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/robusta_data_cleaned.csv'


# We will use pandas.

# In[12]:


import pandas as pd 


# load the data

# In[13]:


coffee_df = pd.read_csv(coffee_data_url,index_col=0)


# In[14]:


type(coffee_df)


# In[15]:


coffee_df.columns


# In[16]:


coffee_df.columns[0]


# In[17]:


len(coffee_df.columns)


# In[18]:


coffee_df.shape


# In[19]:


coffee_df.head()


# In[20]:


coffee_df.head


# In[21]:


coffee_df.head(2)


# In[22]:


coffee_df.tail()


# In[23]:


coffee_df.info()


# In[24]:


coffee_df.columns[42]


# In[25]:


col_types = coffee_df.dtypes


# In[26]:


col_types[:5]


# In[27]:


type(col_types[0])


# In[28]:


for col_name in coffee_df.columns:
    print(col_name[:3])


# In[29]:


my_list = ['honda','ford','nissan']


# In[30]:


type(my_list)


# In[31]:


my_list[-1]


# In[32]:


short_names = [col_name[:3] for col_name in coffee_df.columns]


# In[33]:


type(short_names)


# In[34]:


short_names


# ## Questions After Class
# 
# ### • will we be gathering our own data or will it all be provided for the course?
# 
# ### Will you always give us an answer key for assignments?
# No, but we will always give personalized feedback. 
# 
# ### will we be cleaning data?
# 
# Yes, see the notes from the first class. 
# 
# ### Will we do correlations later?
# Yes
# 
# ### will we go over more imports like pandas?
# Yes, we will use other libraries.  In A2, you'll even import your own code. 
# 
# 
# ### How will datasets be used in conjunction with one another? 
# We will combine data in a few weeks. 
# 
# ### How similar of an alternative to modeling in R exists in python?
# They are both compelte languages so at some level, they can both do all the same things.  Some libraries are easier/better for specific things in one language or the other. 
# 
# ### Will we be working with databases at all in this class?
# 
# A little.  We'll pull from a database into python. 
# 
# ### Are we going going to be using pandas a lot in this class?
# Yes.  We will use pandas for almost every single remaining class session this semester. 
# 
# ### how do you short-cut fill variable names in jupyter
# 
# Press tab to autocomplete 
# 
# 
# ### what is the most efficient way to get help on the homework ?
# Accept the assignment and make an issue or go to office hours for general questions.  For clarifying questions, you can post an issue on the course website.  
# 
# If you are stuck with some progress made, upload (or push) your code first and then ask for help so we can see where you are. 
# 
# ### is there a best or most common way to organize data for use
# 
# csv
# 
# ### how would you laod a csv file with python if i was using visual studio instead of jupyter?
# 
# All of the code we are writing will work in any python environment that has the libraries.  the Editor you use (jupyter vs VSCode vs PyCharm) does not impact what you can do with python.  Which interpreter you use can impact and jupyter does default to ipython instead of the core python kernel, but that does not change how to load data.  
# 
# Remember that jupyter is not on a cloud service. YOu can use any file on your computer with a relative path.
