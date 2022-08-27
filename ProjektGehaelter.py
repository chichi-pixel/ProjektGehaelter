#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Matplotlib config
get_ipython().run_line_magic('matplotlib', 'inline')

#SVG-Anzeige anschalten
get_ipython().run_line_magic('config', "InlineBackend.figure_formats = ['svg']")

#Größe definieren
get_ipython().run_line_magic('config', "InlineBackend.rc = {'figure.figsize': (5.0, 3.0)}")


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns

def convert_to_float(s):
    try:
        return np.float(s)
    except ValueError:
        return np.nan

#https://www.kaggle.com/datasets/kaggle/sf-salaries

df = pd.read_csv("Salaries.csv",
                    converters = {'BasePay': convert_to_float,
                                 'OvertimePay': convert_to_float,
                                 'OtherPay': convert_to_float,
                                 'Benefits': convert_to_float},
                    dtype= {'Status': str})
df.head()
                    


# # Visualisiere die Einkommensverteilung (BasePay oder TotalPayBenefits) für das Jahr 2014!
# 
# 

# In[3]:


base_pay_2014_max = df.loc[df["Year"] == 2014, "BasePay"].max()


# In[4]:


df.loc[df["Year"] == 2014, "BasePay"].min()


# In[5]:


df.loc[df["Year"] == 2012, "BasePay"].min()


# In[6]:


sns.histplot(data=df[df["Year"] == 2014], x = "BasePay", binwidth = 10000, binrange = (0, base_pay_2014_max))


# # Wir möchten nach San Francisco ziehen. Welchen öffentlichen Job sollten wir annehmen, um möglichst viel zu verdienen?
# 
# Der Job muss aber auch "erreichbar" sein für uns, "CAPTAIN III (POLICE DEPARTMENT)" wäre für uns so ohne weiteres vermutlich nicht erreichbar. 
# 
# Ermittle also die häufigsten 10 Jobs (gruppiert nach der Spalte `JobTitle`) und plotte zu jedem JobTitle das durchschnittliche Gesamteinkommen (TotalPayBenefits) für das Jahr 2014 in einem Balkendiagramm. Für welchen Job sollten wir uns bewerben?

# In[13]:


df_2014 = df[df["Year"] == 2014]
df_jobs=df_2014.groupby("JobTitle").agg(count = ("Id", len), avgPay=("TotalPayBenefits", np.mean)).sort_values("count",ascending=False).iloc[:10]
df_jobs.head()


# In[16]:


sns.set()
ax = sns.barplot(x=df_jobs.index, y = df_jobs["avgPay"])
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment="right",
    fontweight="light",
    fontsize="small"
);


# In[17]:


#Google: "rotate label"


# In[ ]:




