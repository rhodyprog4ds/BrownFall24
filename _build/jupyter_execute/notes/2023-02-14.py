#!/usr/bin/env python
# coding: utf-8

# # Tidy Data and Reshaping Datasets

# In[1]:


import pandas as pd
import seaborn as sns

sns.set_theme(palette='colorblind',font_scale=2)


# In[2]:


url_base = 'https://raw.githubusercontent.com/rhodyprog4ds/rhodyds/main/data/'

datasets = ['study_a.csv','study_b.csv','study_c.csv']


# In[3]:


list_of_df = [pd.read_csv(url_base + dataset,na_values='-') for dataset in datasets]


# In[4]:


list_of_df[0]


# In[5]:


list_of_df[1]


# In[6]:


list_of_df[2]


# In[7]:


list_of_df[2].mean()


# In[8]:


sum([16,3,2,11,1])/5


# In[9]:


sum([16,3,2,11,1,0])/6


# In[10]:


list_of_df[2].groupby('treatment').mean()


# In[11]:


list_of_df[2].groupby('person').mean()


# In[12]:


dfa = list_of_df[0]
dfa


# In[13]:


dfa.melt(id_vars=['name'],var_name='treatment',value_name='result')


# In[14]:


arabica_data_url = 'https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/arabica_data_cleaned.csv'
# load the data
coffee_df = pd.read_csv(arabica_data_url)
# get total bags per country
bags_per_country = coffee_df.groupby('Country.of.Origin')['Number.of.Bags'].sum()

# sort descending, keep only the top 10 and pick out only the country names
top_bags_country_list = bags_per_country.sort_values(ascending=False)[:10].index

# filter the original data for only the countries in the top list
top_coffee_df = coffee_df[coffee_df['Country.of.Origin'].isin(top_bags_country_list)]


# In[15]:


bags_per_country


# In[16]:


top_bags_country_list


# In[17]:


top_coffee_df.head(1)


# In[18]:


coffee_df.head(1)


# In[19]:


coffee_df.shape,top_coffee_df.shape


# In[20]:


top_coffee_df.describe()


# In[21]:


top_coffee_df.columns


# In[22]:


ratings_of_interest = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body',
       'Balance', ]
coffe_scores_df = top_coffee_df.melt(id_vars='Country.of.Origin',value_vars=ratings_of_interest,
                   var_name='rating',value_name='score')
coffe_scores_df.head(1)


# In[23]:


top_coffee_df.melt(id_vars='Country.of.Origin')['variable'].unique()


# In[24]:


top_coffee_df.melt(id_vars='Country.of.Origin',value_vars=ratings_of_interest,)['variable'].unique()


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


sns.displot(data=coffe_scores_df, x='score',col='Country.of.Origin',
           hue = 'rating',col_wrap=5,kind='kde')


# In[27]:


sns.displot(data=coffe_scores_df, x='score',hue='Country.of.Origin',
           col = 'rating',col_wrap=3,kind='kde')


# In[28]:


top_coffee_df.columns


# In[29]:


coffe_scores_df2= top_coffee_df.melt(id_vars=['Country.of.Origin','Color'],value_vars=ratings_of_interest,
                   var_name='rating',value_name='score')
coffe_scores_df2.head(1)


# In[30]:


sns.displot(data=coffe_scores_df2, x='score',hue='Country.of.Origin',
           col = 'rating',row='Color',kind='kde')


# In[31]:


coffee_df.describe()


# ## More manipulations
# 
# Here, we will make a tiny `DataFrame` from scratch to illustrate a couple of points

# In[32]:


large_num_df = pd.DataFrame(data= [[730000000,392000000,580200000],
                                   [315040009,580000000,967290000]],
                           columns = ['a','b','c'])
large_num_df


# This dataet is not tidy, but making it this way was faster to set it up.  We could make it tidy using melt as is.

# In[33]:


large_num_df.melt()


# However, I want an additional variable, so I wil reset the index, which adds an index column for the original index and adds a new index that is numerical. In this case they're the same.

# In[34]:


large_num_df.reset_index()


# If I melt this one, using the index as the `id`, then I get a reasonable tidy DataFrame

# In[35]:


ls_tall_df = large_num_df.reset_index().melt(id_vars='index')
ls_tall_df


# Now, we can plot.

# In[36]:


sns.catplot(data = ls_tall_df,x='variable',y='value',
            hue='index',kind='bar')


# Since the numbers are so big, this might be hard to interpret.  Displaying it with all the 0s would not be easier to read.  The best thing to do is to add a new colum with adjusted values and a corresponding title.

# In[37]:


ls_tall_df['value (millions)'] = ls_tall_df['value']/1000000
ls_tall_df.head()


# Now we can plot again, with the smaller values and an updated axis label.  Adding a column with the adjusted title is good practice because it does not lose any data and since we set the value and the title at the same time it keeps it clear what the values are.

# In[38]:


sns.catplot(data = ls_tall_df,x='variable',y='value (millions)',
            hue='index',kind='bar')


# In[ ]:




