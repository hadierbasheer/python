#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import regex as re
import requests
import sys
if sys.version_info[0] < 3:
     from StringIO import StringIO
else:
     from io import StringIO
cdd_url = "http://cdd.publicsafety.gc.ca/dl-eng.aspx?cultureCode=en-Ca&normalizedCostYear=1"
req = requests.get(cdd_url)
data = req.text
data_new = data.replace("*", "")
data_new = re.sub(r"\.\s*\n+", ". ", data_new)
df = pd.read_csv(StringIO(data_new), sep="\t")


# In[5]:


df.head()


# In[7]:


# Check how many distinct values in the "EVENT CATEGORY" column
df["EVENT CATEGORY"] . nunique()


# # Issue with directly loading it as DataFrame

# In[17]:


df = pd.read_csv(cdd_url, delimiter="\t")


# In[19]:


df


# In[18]:


df["EVENT CATEGORY"].nunique()


# # Solution for getting rid of incorrect return

# In[22]:


# Read the data as plain text rather than DataFrame (hint: use requests)
req_result = requests.get(cdd_url)
data = req_result.text


# In[23]:


# Ctrl + F to check a few examples in the EVENT CATEGORY column, and find the pattern 
data


# In[25]:


# Find all the cases where the similar pattern are observed in the text (hint: use regex)
# Very useful link: https://www.w3schools.com/python/python_regex.asp
#  ". \n\n"
# ".\n"
#".     \n\n\ "
data_new = re.sub(r"\.\s*\n+", ". ", data)


# In[26]:


# Get rid of the carriage return
data_new


# In[27]:


# Create dataframe from the new edited text
df = pd.read_csv(StringIO(data_new), sep="\t")


# In[28]:


# Check how many distinct values in the "EVENT CATEGORY" column
df["EVENT CATEGORY"].nunique()


# In[29]:


# Check what are the distinct values in the "EVENT CATEGORY" column
df["EVENT CATEGORY"].unique()


# # Make it as a script

# In[ ]:


import pandas as pd
import regex as re
import requests
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
cdd_url = "http://cdd.publicsafety.gc.ca/dl-eng.aspx?cultureCode=en-
Ca&normalizedCostYear=1"
req = requests.get(cdd_url)
data = req.text
data_new = data.replace("*", "")
data_new = re.sub(r"\.\s*\n+", ". ", data_new)
df = pd.read_csv(StringIO(data_new), sep="\t")

