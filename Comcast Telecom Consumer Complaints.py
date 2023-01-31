#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the Module

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Read the csv file

df=pd.read_csv(r'E:\Data Science with Python Simplilearn\\Comcast_telecom_complaints_data.csv')
df.head()


# In[3]:


# Observing the data information in column wise

df.info()


# In[4]:


# Converting date column from object to datetime format by using predefined function

df['Date']=pd.to_datetime(df['Date'])
df.info()


# In[5]:


# Adding New Column "month"

df['month']=df['Date'].dt.month_name()
df


# In[6]:


# Finding no. of complaints per day

df['Date'].value_counts()


# In[7]:


# Grouping the date size to find the no of complaint in the record

dates=df.groupby('Date').size()
dates


# In[8]:


# Reset and Renaming the dates column name to find the count of compalints

daily=pd.DataFrame(dates).reset_index()
daily=daily.rename(columns={0:'count'})
daily


# In[9]:


# creating plot graph to understand the month wise complaint

daily.plot(x='Date',y='count',kind='line',color='green')


# In[10]:


# Grouping the maximum complaint record months of data

month=df.groupby('month').size()
month


# In[11]:


# Reset and Renaming the month column name to find the count of compalints

month=pd.DataFrame(month).reset_index()
month=month.rename(columns={0:'count'})
month


# In[12]:


# Using Bar graph for month column to identitfy the no. of complaint records on the month

month.plot(x='month',y='count',kind='bar')


# In[13]:


# Identify the complaint category by using value_counts function

df['Customer Complaint'].value_counts()


# In[14]:


# Using Lambda function to changing the string items upper case in each words

df['Customer Complaint']=df['Customer Complaint'].apply(lambda x : x.title())
df['Customer Complaint'].value_counts()


# In[15]:


# Finding the most complaints category of "Customer Complaint" by using plot bar graph

df['Customer Complaint'].value_counts()[:10].plot.bar()


# In[16]:


# Recall the dataset

df


# In[17]:


# Identify the complaints by using string contains by keywords

internet_issues1=df[df['Customer Complaint'].str.contains('Network')].count()
internet_issues2=df[df['Customer Complaint'].str.contains('Network')].count()
internet_issues3=df[df['Customer Complaint'].str.contains('Internet')].count()
total_internet=internet_issues1+internet_issues2+internet_issues3
total_internet


# In[18]:


# Identify the complaints by using string contains by keywords

billing_issue1=df[df['Customer Complaint'].str.contains('Billing')].count()
billing_issue2=df[df['Customer Complaint'].str.contains('Charges')].count()
total_billing=billing_issue1+billing_issue2
total_billing


# In[19]:


# Identify the complaints by using string contains by keywords

service_issue1=df[df['Customer Complaint'].str.contains('Service')].count()
service_issue2=df[df['Customer Complaint'].str.contains('Customer')].count()
total_service=service_issue1+service_issue2
total_service


# In[20]:


# Identify the complaints by using string contains by keywords.

other_issue=2224-(total_billing+total_internet+total_service)
other_issue


# In[21]:


# Findind the status column unique String values

df['Status'].unique()


# In[22]:


# Modifying the status column by using if else conditon

df['New_Status']=[ "Open" if x=="Open" or x=="Pending" else "Closed" for x in df['Status']]


# In[23]:


df


# In[24]:


# Finding the staus of complaint by state wise and fill the NaN by using fillna()

state_complain=df.groupby(['State','New_Status']).size().unstack().fillna(0)
state_complain


# In[25]:


# creating stack bar graph for finding the state wise complaint

state_complain.plot.bar(stacked=True,figsize=(10,6))


# In[26]:


# Findly the top complaint states by using value count function

df['State'].value_counts()[:5]


# In[27]:


# Grouping the unresolved data by using groupby function.
# filling the missing values by using fillna function.
# sort the 'Open' values by using sort_values function

unresolved_data=df.groupby(['State','New_Status']).size().unstack().fillna(0).sort_values(by='Open')
unresolved_data


# In[28]:


# Showing the unresolved data by using percentage method

unresolved_data['unresolved_cmp_perct']=unresolved_data['Open']/unresolved_data['Open'].sum()
unresolved_data


# In[29]:


# Grouping the complaint by using 'Received Via'and 'New_Status' column

resolved_data=df.groupby(['Received Via','New_Status']).size().unstack()
resolved_data


# In[30]:


# Finding the resolved data by using percentage

resolved_data['resolved']=resolved_data['Closed']/resolved_data['Closed'].sum()*100
resolved_data['resolved']

