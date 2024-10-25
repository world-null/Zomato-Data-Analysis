#!/usr/bin/env python
# coding: utf-8

# # Zomato_Data_Analysis_Project

# In[2]:


import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import seaborn as sns 


# In[4]:


df=pd.read_csv("E:/CODING/project/DataSetVisualizeton/Zomato data .csv")
df


# In[6]:


def handlerate(value):
    value = value.split("/")  
    value = value[0]
    return float(value)

df["rate"] = df["rate"].apply(handlerate)
df


# In[8]:


df.info


# # Type_of_resturant

# In[9]:


sns.countplot(x=df["listed_in(type)"])
plt.xlabel("types of resturant")


# In[12]:


grpdata=df.groupby("listed_in(type)")["votes"].sum()
result = pd.DataFrame({"votes":grpdata})
plt.plot(result,c="green",marker="o")
plt.xlabel("Types_of_resturant", c="red",size=20)
plt.ylabel("votes",c="red",size=20)


# In[17]:


plt.hist(df["rate"],bins=10)
plt.title("rating distribution")
plt.show


# # Avg_order spending by couples

# In[18]:


coupleData=df["approx_cost(for two people)"]
sns.countplot(x=coupleData)


# # Which mode recives maximum rating 

# In[19]:


plt.figure(figsize=(6,6))
sns.boxplot(x="online_order", y="rate", data=df)


# # Resturant and mode of orders

# In[23]:


pivot_table=df.pivot_table(index="listed_in(type)", columns="online_order", aggfunc="size", fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu",fmt="d")
plt.title("heatmap")
plt.xlabel("online order")
plt.ylabel("listed_in(type)")
plt.show()


# In[ ]:




