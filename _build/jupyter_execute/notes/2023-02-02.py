#!/usr/bin/env python
# coding: utf-8

# # Pandas and Indexing
# 
# ## Iterable types

# In[1]:


a = [char for char in 'abcde']
b = {char:i for i,char in enumerate('abcde')}
c = ('a','b','c','d','e')
d = 'a b c d e'.split()


# In[2]:


a


# In[3]:


type(a)


# In[4]:


b


# In[5]:


type(b)


# In[6]:


c


# In[7]:


type(c)


# In[8]:


d


# In[9]:


type(d)


# ## Reading data other ways

# In[10]:


import pandas as pd


# In[11]:


course_comms_url = 'https://rhodyprog4ds.github.io/BrownSpring23/syllabus/communication.html'


# THis reads in from the html directly.

# In[12]:


pd.read_html(course_comms_url)


# In[13]:


html_list = pd.read_html(course_comms_url)


# In[14]:


type(html_list)


# In[15]:


type(html_list[0])


# In[16]:


[type(h) for h in html_list]


# In[17]:


achievements_url = 'https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html'


# get the tables

# In[18]:


achievements_df_list = pd.read_html(achievements_url)


# make a list means use a list comprehension

# In[19]:


[ach.shape for ach in achievements_df_list]


# In[20]:


achievements_df_list.shape


# In[21]:


coffee_data_url = 'https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/robusta_data_cleaned.csv'


# In[22]:


coffee_df = pd.read_csv(coffee_data_url,index_col=0)


# In[23]:


coffee_df.head(1)


# In[24]:


coffee_df['Species'].head()


# In[25]:


type(coffee_df['Species'])


# In[26]:


coffee_df.columns


# In[27]:


coffee_df['Number.of.Bags']


# In[28]:


new_values = {0:'<100',1:'100-199',2:'200-299',3:'300+'}


# In[29]:


[new_values[int(num/100)] for num in coffee_df['Number.of.Bags']]


# In[30]:


bags_bin = lambda num: int(num/100)
[new_values[bags_bin(num)] for num in coffee_df['Number.of.Bags']]


# In[31]:


type(pd.read_csv)


# In[32]:


type(bags_bin)


# ## Importing locally
# 
# If I make a file in the same folder as my notebook called `example.py`
# and then put

# In[33]:


get_ipython().run_cell_magic('bash', '', 'cat example.py\n')


# in the file, we can use that file like:

# In[34]:


from example import name


# In[35]:


name


# In[36]:


import example


# In[37]:


example.name


# In[ ]:





# ## Questions After Class
# 
# ### why does casting the int over the (num/100) give you the right number? Is it because of floor division?
# 
# First let's look at an interim value, lets pick a value for `num`

# In[38]:


num = 307


# Then do the calculation without casting to int

# In[39]:


num/100


# Remember that `int` type is an integer or whole number, no fraction.  So, casting drops the decimal part. 
# 
# 
# ###  How would adding 2 DataFrametogether of separate types affect the type command?
# 
# It depends what "add" means.  If addition it might error, but if it worked, then it would still be a DataFrame. If stacking with `pd.concat` it would also be a DatFrame. 
# 
# If you make them into a list, then the would be a list. 
# 
# 
# 
# ### what keys to use in the dictionaries?
# In the assignment the instruction say
# 
# ### how to save as a local csv file?
# 
# [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
# 
# ### how to create a Dataframe?
# 
# Use the [constructor](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
# 
# 
# ### how to read using relative path?
# 
# A relative path can work just like a URL. [read about them here](https://www.redhat.com/sysadmin/linux-path-absolute-relativehttps://www.redhat.com/sysadmin/linux-path-absolute-relative)
# 
# ### I would like to know about other common forms of data files.
# 
# The pandas documentation's [I/O](https://pandas.pydata.org/docs/user_guide/io.html) page is where I recommend starting
# 
# ## What other libraries do we end up using?
# 
# Next week we will use `seaborn` for plotting. Later in the semester we will use `sklearn` for machine learning.  We will use a few other libaries for a few features, but these three are the main ones.
