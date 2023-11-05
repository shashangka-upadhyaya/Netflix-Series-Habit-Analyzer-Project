#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv('convertcsvs.csv')


# In[3]:


df.head(26)


# In[40]:


df.info


# In[4]:


df.shape


# In[5]:


# Analyzing personal netflix data in python pandas 

import pandas as pd

df = pd.read_csv('convertcsvs.csv', index_col='Profile Name')


# In[6]:


df.head(26)


# In[7]:


df.info()


# In[8]:


df.describe()


# Preparing data for data analysis 
# Now Data Cleaning is done 
# 
# First, we'll start by dropping the columns we're not planning to use.
# it can be nice to work with a dataframe that includes only columns we're actually using.

# In[9]:


#checking datatype of this data we use the following code 
df.dtypes


# In[10]:


df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df.dtypes


# In[23]:


df.info


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib


# In[13]:


# change the Start Time column into the dataframe's index
df = df.set_index('Start Time')

# convert from UTC timezone to eastern time
df.index = df.index.tz_convert('US/Eastern')

# reset the index so that Start Time becomes a column again
df = df.reset_index()

#double-check that it worked
df.head(1)


# In[14]:


df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes


# In[23]:


# create a new dataframe called office that that takes from df
# only the rows in which the Title column contains 'The Office (U.S.)'
office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]


# In[24]:


office.shape


# In[25]:


office = office[(office['Duration'] > '0 days 00:01:00')]
office.shape


# In[26]:


office['Duration'].sum()


# In[27]:


office['weekday'] = office['Start Time'].dt.weekday
office['hour'] = office['Start Time'].dt.hour

# check to make sure the columns were added correctly
office.head(1)


# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib


# In[29]:


# set our categorical and define the order so the days are plotted Monday-Sunday
office['weekday'] = pd.Categorical(office['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)

# create office_by_day and count the rows for each weekday, assigning the result to that variable
office_by_day = office['weekday'].value_counts()

# sort the index using our categorical, so that Monday (0) is first, Tuesday (1) is second, etc.
office_by_day = office_by_day.sort_index()

# optional: update the font size to make it a bit larger and easier to read
matplotlib.rcParams.update({'font.size': 22})

# plot office_by_day as a bar chart with the listed size and title
office_by_day.plot(kind='bar', figsize=(20,10), title='Quantum Chronices Episode Watched by Day')


# In[22]:


# set our categorical and define the order so the hours are plotted 0-23
office['hour'] = pd.Categorical(office['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

# create office_by_hour and count the rows for each hour, assigning the result to that variable
office_by_hour = office['hour'].value_counts()

# sort the index using our categorical, so that midnight (0) is first, 1 a.m. (1) is second, etc.
office_by_hour = office_by_hour.sort_index()

# plot office_by_hour as a bar chart with the listed size and title
office_by_hour.plot(kind='bar', figsize=(20,10), title='Stranger Things (Season 3)  Watched by Hour')


# In[ ]:




