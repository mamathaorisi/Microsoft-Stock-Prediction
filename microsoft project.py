#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("MSFT.csv")
df


# In[ ]:


df = df[["Date", "Close"]]
df


# In[ ]:


import datetime
def str_to_datetime(s):
    split=s.split("-")
    year, month,day = int(split[0]), int(split[1]), int(split[2])
    return datetime.datetime(year=year, month=month, day=day)

datetime_object = str_to_datetime("2021-06-28")
datetime_object


# In[ ]:


df


# In[ ]:




