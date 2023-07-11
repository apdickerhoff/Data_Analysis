#!/usr/bin/env python
# coding: utf-8

# # How to calculate summary statistics?
# 
# Follow along with this [article](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html). The data set from the article has been included in the repository already, no need to download separately. This notebook will also contain some supplemental information to help you better understand basic summary statistics.
# 
# First thing we want to do is to import the pandas library.

# In[1]:


# import the pandas library and use the alias 'pd'
import pandas as pd


# We are going to be working with the titanic dataset found [here.](https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv) It is in csv format and consists fo the following data columns:

# 
# - PassengerId: Id of every passenger.
# - Survived: Value of 0 for not survived and 1 for survived.
# - Pclass: There are 3 classes: Class 1, Class 2 and Class 3.
# - Name: Name of passenger.
# - Sex: Gender of passenger.
# - Age: Age of passenger.
# - SibSp: Number of siblings / spouses on the Titanic
# - Parch: Number of parents / children on the Titanic
# - Ticket: Ticket number of passenger.
# - Fare: Indicating the fare.
# - Cabin: The cabin of passenger.
# - Embarked: Port of Embarkation ( C = Cherbourg, Q = Queenstown, S = Southampton)
# 
# Let's load the data into a data frame and see what the data looks like. Since your csv file is in a folder named data, the path syntex is: data/your_data_set_name.csv to read your data into a data frame.

# In[2]:


#read titantic data set into a data frame

df = pd.read_csv('/Users/apdic/Data Analysis/titanic.csv')
#although we listed the column names above, write the code to return the name of all of your columns in the dataset


# In[3]:


# print the first 5 rows from the dataframe
df.head()


# What are some of your observations from looking at the data so far? Questions you would like to explore?
# 
# For example: I noticed that Survived is an int instead of Yes or No, not sure if I'll need to address that while data cleaning. I'm curious if the amount you paid for your ticket(Fare) impacted your survival rate?
# <br><br><br><br><br>
# 
# 
# 
# 
# 
# 

# In[4]:


df.info() 
#returns: 
#name of the column, Non-null Count meaning how many non-null values their are in that column and Dtype
#int64 means int value, float64 means float value, object means string value.


# By default statistical anaysis is run on numerical values.  
# 
# Looking at the data above what do you notice about Age? Cabin? Hint: It would appear we are missing some data. How might these observations influence the questions asked?<br><br>
# 
# Any other observations?
# <br><br><br>

# ## Aggregating statistics

# ### Calculating Mean, Median, Mode

# #### Mean: is the sum of the values divided by the number of values.

# In[10]:


#What is the mean age of the Titanic passengers?
df['Age'].mean()


# We can also get the mean for all columns. 

# In[6]:


#mean for all columns
df.mean()


# #### Median: Is the middle value when all the numbers are put in order, dividing the sample into two halves.  
# 
# Example: (23, 46, 55, 78, 99)<br> 
# The Median of the above example is 55. 

# In[12]:


# What is the median age and ticket fare price of the Titanic passengers?
df['Age'].median()
df['Fare'].median()


# #### Mode: The most frequent value(s) in a sample

# In[13]:


# What is the mode age and fare for the titanic dateset?
df['Age'].mode()
df['Fare'].mode()


# Note the difference between Mean, Medium and Mode.  Why is this important? Can you think of times you would what to use one over the others?<br><br><br><br><br>
# 
# 
# 
# 
# 

# We can use the .describe() funciton to display some basic statistics for all numeric columns:

# In[14]:


# Summary statistics for all columns in a dataset
df.describe()


# In[21]:


# Summary statistics for just the Age and Fare columns
df['Age'].describe()
df['Fare'].describe()


# Notice that medium and mode are not included in .describe()
# 
# Instead of the predefined statistics, specific combinations of aggregating statistics for given columns can be defined using the [DataFrame.agg() method:](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg)

# In[ ]:


#use .agg


# ## Aggregating statistics grouped by category

# Calculating a given statistic (e.g. mean age) for each category in a column (e.g. male/female in the Sex column) is a common pattern. The groupby method is used to support this type of operations. 

# In[ ]:


# What is the average age for male versus female Titanic passengers?


# In[ ]:


# What is the survival of men verses female Titanic Passengers? 



# In[ ]:


# Try some other combinations, what do you think about this method?









# In the previous examples, we explicitly selected the 2 columns first. If not, the mean method is applied to each column containing numerical columns:

# In[ ]:


#use .groupby Sex and .mean


# It does not make much sense to get the average value of the Pclass. if we are only interested in the average age for each gender, the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well:

# In[ ]:


#use .goupby Sex just for Age 


# In[ ]:


# What is the mean ticket fare price for each of the sex and cabin class combinations?


# In[ ]:


# Try some other combinations, what do you think about this method?






# ## Count number of records by category
# 
# The value_counts() method counts the number of records for each category in a column.

# In[ ]:


# What is the number of passengers in each of the cabin classes?


# The function is a shortcut, as it is actually a groupby operation in combination with counting of the number of records within each group:

# In[ ]:


#Count the number of passengers by cabin classes using groupby


# In[ ]:


# Using the value_counts method what else could you count?





