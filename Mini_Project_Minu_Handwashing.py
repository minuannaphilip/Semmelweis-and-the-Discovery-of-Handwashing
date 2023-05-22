#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mtp
import seaborn as sns


# In[ ]:





# In[2]:


yearly = pd.read_csv(r"C:\Users\user\Documents\Technocolab\yearly_deaths_by_clinic.csv")
print(yearly)


# In[3]:


yearly[['year','births']] 


# In[4]:


yearly["proportion_deaths"] = yearly["deaths"]/yearly["births"]
print (yearly["proportion_deaths"])


# In[5]:


#Task2


# In[ ]:





# In[6]:


yearly1 = yearly.loc[yearly['clinic']=='clinic 1']
yearly1.head()
yearly2 = yearly.loc[yearly['clinic']=='clinic 2']
yearly2.head()


# In[7]:


#Task 3


# In[8]:


ax = yearly1.plot(x="year", y="proportion_deaths",
              label="yearly1")
yearly2.plot(x="year", y="proportion_deaths",
         label="yearly2.", ax=ax)
ax.set_ylabel("proportion_deaths")


# In[9]:


# Task4


# In[10]:


monthly = pd.read_csv(r"C:\Users\user\Documents\Technocolab\monthly_deaths.csv",parse_dates=["date"])
monthly


# In[11]:


monthly.head()


# In[12]:


monthly['proportion_deaths'] = monthly['deaths'] /monthly['births']
monthly['proportion_deaths']


# In[13]:


#Task 5


# In[14]:


ax = monthly.plot(x="date", y="proportion_deaths",
              label="proportion_deaths")
ax.set_ylabel('proportion_deaths')


# In[15]:


#bef_handwashing_date = monthly['date']<= '01-06-1847'
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
bef_handwashing_date = monthly[monthly['date'] < '1847-06-01']
after_handwashing_date = monthly[monthly['date'] > '1847-06-01']
bef_handwashing_date
after_handwashing_date


# In[ ]:





# In[16]:


ax= bef_handwashing_date.plot(x= 'date' ,y='proportion_deaths', label ='before washing')
after_handwashing_date.plot(x='date',y='proportion_deaths',label ='after washing',ax=ax)


# In[17]:


before_proportion = bef_handwashing_date['proportion_deaths']
before_proportion


# In[18]:


after_proportion = after_handwashing_date['proportion_deaths']
after_proportion


# In[19]:


mean_diff = after_proportion.mean() - before_proportion.mean() 


# In[20]:


mean_diff


# In[24]:


# A bootstrap analysis of the reduction of deaths due to handwashing
# We can also do this by numpy.random.choice
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)                                   
    boot_mean_diff.append(boot_after.mean() - boot_before.mean()) 
    

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
pd.Series(boot_mean_diff)
confidence_interval


# In[22]:


doctors_should_wash_their_hands = True

