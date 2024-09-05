#!/usr/bin/env python
# coding: utf-8

# # Web Scraping

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# ````{warning}
# If it says it cannot load one of the libraries, use pip inside your notebook to install, then restart your kernel (Kernel menu, choose restart)
# 
# ```
# pip install beautifulsoup4
# ```
# ````
# 
# ## Getting Data From Websites 
# 
# 
# We have seen that `read_html` can get content from an actual website, not a data file that is hosted somewhere on the internet, that takes tables on a website and returns a list of DataFrames.
# 
# ````{margin}
# ```{note}
# This has a long output, so I hid it by default, but you can view it
# ```
# ````

# In[2]:


pd.read_html('https://rhodyprog4ds.github.io/BrownSpring23/syllabus/achievements.html')


# This gives us a list of DataFrames that come from the website.  `pandas` gets tables by looking in the html for the site and finding the `<table>` tags. 
# 
# 
# ## Everything is Data
# 
# For the purpose of this class, it is best to think of the content on a web page like a datastructure.  
# 
# ![html anatomy](https://cdn2.hubspot.net/hub/53/file-1519188549-jpg/blog-files/webpage-setup.jpg)
# 
# 
# ![HTML tree structure](http://www.w3schools.com/js/pic_htmltree.gif)
# 
# there are tags `<>` that define the structure, and these can be further classified with `classes`
# 
# 
# 
# ## Scraping a URI website
# 
# 
# We're going to create a DataFrame about URI CS & Statistics Faculty.
# 
# from the [people page](https://web.uri.edu/cs/people/) of the department website.
# 
# ````{margin}
# ```{note}
# the inspect link goes to instructions for different browsers
# ```
# ````
# We can [inspect](https://blog.hubspot.com/website/how-to-inspect) the page to check that it's well structured.  
# 
# ```{warning}
# With great power comes great responsibility.
# 
# - always check the [robots.txt](https://web.uri.edu/robots.txt)
# - do not do things that the owner says not to do
# - government websites are typically safe
# ```
# 
# 
# We'll save the URL for easy use
# 
# Then we can use the `requests` library to make a call to the internet.  It actually gets back a [response object](https://requests.readthedocs.io/en/latest/api/#requests.Response) which has a lot of extra information.  For today we only need the `content` from the page which is an attrtibute of that object

# In[3]:


cs_people_url = 'https://web.uri.edu/cs/people/'
cs_people_html = requests.get(cs_people_url).content

cs_people = BeautifulSoup(cs_people_html,'html.parser')


# This is raw: 
# ````{margin}
# ```{note}
# here I suppressed th output in class by looking only at the first few characters
# ```
# ````

# In[4]:


cs_people_html[:100]


# But we do not need to manually write search tools, that's what [`BeautifulSoup`](https://beautiful-soup-4.readthedocs.io/en/latest/) is for.

# In[5]:


cs_people


# ### Looking at tags 
# 
# In this object we can use any tag from the file and get back the first instance

# In[6]:


cs_people.a


# In[7]:


cs_people.div


# In[8]:


cs_people.h3


# this [cheatsheet](https://web.stanford.edu/group/csp/cs21/htmlcheatsheet.pdf) shows lots of html tags, but for this purpose you do not really need it. You'll be inspecting the page and then looking for what you want
# 
# ### Searching the source
# 
# 
# More helpful is the `find_all` method we wnat to find all `div` tags that are "peopleitem" class. We decided this by inspecting the code on the website.

# In[9]:


cs_people.find_all('div','peopleitem')


# this is a long, object and we can see it looks iterable (`[` at the start)

# In[10]:


people_items = cs_people.find_all('div','peopleitem')
len(people_items)


# ```{important}
# answer to questions about searching [from the docs](https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_all#the-keyword-arguments)
# ```

# In[11]:


type(people_items)


# We can also look at only the first instance

# In[12]:


people_items[0]


# We notice that the name is inside a `<h3>` tag with class `p-name` and then inside an a tag after that.  We also know from looking at the overall page that there are lots of other a tags, so we do not want to search all of those.

# In[13]:


people_items[0].find('h3','p-name').a.string


# Then we can use a list comprehension to build alist of them.

# In[14]:


names = [name.a.string for name in cs_people.find_all('h3','p-name')]
names


# In[15]:


people_items[0]


# In[16]:


people_items[0].find('p','people-title').string


# How to pull out the titles for each person (eg Assitatn Teaching Professor, Associate Professor)

# In[17]:


titles = [t.string for t in cs_people.find_all("p","people-title")]


# In[18]:


titles


# on one item, the `p` tag seems to work, but that is because the tag gives only the first instance,

# In[19]:


people_items[0].find('p')


# but we see if we ust this for all, it is way more informaiton than we were looking for.

# In[20]:


[t.string for t in cs_people.find_all("p")]


# We can pull out two more things, the people-department indicates who is CS & who is Statistics.

# In[21]:


disciplines = [d.string for d in cs_people.find_all("p",'people-department')]
emails = [e.string for e in cs_people.find_all("a",'u-email')]


# In[22]:


css_df = pd.DataFrame({'name':names, 'title':titles,'e-mails':emails, 'discipline':disciplines})
css_df.head()


# ## Crawling and scraping
# 
# Remember we pulled the names out of links, when in the browser, we click on the links, we see that they are to a profile page. On these pages, they have the office number.  Let's add those to our dataframe. 
# 
# First, we will do it for one person, then make a loop.

# In[23]:


people_items[0].find('h3','p-name').a


# We see that the information that we want is in the `href` attribute, to read that, we check the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes). This tells us there is a `.attrs` attribute of the python object we are working with.

# In[24]:


people_items[0].find('h3','p-name').a.attrs


# It's a dictionary and the attribute we want is the key we want. Nowe, we do the same thing we did above, request, pull the content from the response and then use the parser.

# In[25]:


alvarez_url = people_items[0].find('h3','p-name').a.attrs['href']
alvarez_html = requests.get(alvarez_url).content
alvarez_info = BeautifulSoup(alvarez_html,'html.parser')


# then we find the tag and class we need from inspecting and pull that.

# In[26]:


alvarez_info.find_all('li','people-location')


# it's an interable, so we pull the item out

# In[27]:


alvarez_info.find_all('li','people-location')[0]


# Then we get the content.

# In[28]:


alvarez_info.find_all('li','people-location')[0].string


# this time this doesn't work, so we can use the python `__dict__` to inspect the object and see where it stored what we want.

# In[29]:


alvarez_info.find_all('li','people-location')[0].__dict__


# it's the second elment of content

# In[30]:


alvarez_info.find_all('li','people-location')[0].contents[1]


# Now tht we know how to do it, we can put it in a loop.

# In[31]:


offices = []
for name_link in cs_people.find_all('h3','p-name'):
    url = name_link.a.attrs['href']
    person_html = requests.get(url).content
    person_info = BeautifulSoup(person_html,'html.parser')
    try: 
        offices.append(person_info.find_all('li','people-location')[0].contents[1])
    except:
        offices.append(pd.NA)


css_df['office'] = offices


# We got an error at first, so we added the [`try` and `except`](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) to handle when there is no office location.

# In[32]:


css_df.head()


# In[33]:


css_df.to_csv('css_faculty.csv')


# In[ ]:





# ## Questions after class
# 
# ### what does .a do?
# it gives the first instance of the `<a>` tag 
# 
# ### is it worth it to try and web scrape a page that is poorly written?
# 
# If it is important information.  In these cases, you might have to do more manual parsing or even some manual fixes. 
# 
# For this class, no. 
# 
# ### In theory, you could parse images and potentially their metadata with this method?
# 
# This method could be a way to download images and the text that is around them, yes.  This is how a lot of image datasets are built for machine learning. 
# 
# ### Is API the website's way of specify what information it will allow for you have? 
# 
# What we did today did not use any API.  An API call would use the request library, and similar patterns to what we did, espeically the end of class. However and API call would typically respond with json, not html. 
# 
# ### In the web-scraping of the offices, there were two strings, 'CBLS 377', and 'CBLS Building 487' how would we use pandas to normalize things like this?”
# 
# We could use the `replace` method that we used last week.
