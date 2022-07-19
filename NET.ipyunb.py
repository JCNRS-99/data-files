#!/usr/bin/env python
# coding: utf-8

# ![netflix-4.jpg](attachment:netflix-4.jpg)

# # Netflix, Inc. is an American subscription streaming service and production company. Launched on August 29, 1997, it offers a film and television series library through distribution deals as well as its own productions, known as Netflix Originals.

# # NETFLIX DATASET 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib. pyplot as plt
import seaborn as sns 


# In[3]:


netflix_data= pd.read_csv("https://raw.githubusercontent.com/JAYACHITRA2199/data-files/PYTHON-FILES/8.%20Netflix%20Dataset.csv")
netflix_data


# In[4]:


netflix_data.head()


# In[5]:


netflix_data.tail()


# # Removing and Replacing Null values in dataset:

# In[6]:


netflix_data.shape


# In[7]:


netflix_data.columns


# In[8]:


netflix_data.duplicated().sum()


# In[9]:


netflix_data.isnull().sum()


# In[10]:


netflix_data.info()


# In[11]:


netflix_data.describe()


# In[12]:


netflix_data.nunique()


# In[13]:


netflix_data.dropna()


# In[14]:


netflix_data[netflix_data.duplicated()]
netflix_data


# In[ ]:





# In[15]:


df = pd.read_csv("https://raw.githubusercontent.com/JAYACHITRA2199/data-files/PYTHON-FILES/8.%20Netflix%20Dataset.csv")

print(df.corr())


# In[16]:


netflix_data.Category.unique()


# In[17]:


netflix_data.Director.unique()


# In[18]:


netflix_data.Type.unique()


# In[19]:


netflix_data.Type.value_counts()


# # DATA VISUALLTION

# In[20]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


plt.figure(figsize=(15,6))
sns.countplot('Category',data=netflix_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[22]:


plt.figure(figsize=(15,6))
sns.countplot('Type',data=netflix_data,palette='hls')
plt.xticks(rotation=40)
plt.show()


# In[23]:


plt.figure(figsize=(15,6))
sns.countplot('Rating',data=netflix_data,palette='hls')
plt.xticks(rotation=40)
plt.show()


# In[ ]:





# In[ ]:




