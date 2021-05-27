#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('BankNote_Authentication.csv')
df.head()


# In[3]:


X = df.iloc[:,:-1]
y = df.iloc[:,-1:]


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# In[6]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train,y_train)


# In[7]:


y_pred = model.predict(X_test)


# In[8]:


from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)


# In[9]:


score


# In[10]:





# In[ ]:




