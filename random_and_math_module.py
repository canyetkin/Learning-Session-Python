#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
random and math modules*****
"""


# In[1]:


import random


# In[2]:


random.__dir__()


# In[3]:


help(random)


# In[4]:


random.random()


# In[6]:


random.uniform(2,6)


# In[7]:


random.randint(2,9)


# In[9]:


random.choice([*range(10)])


# In[10]:


random.choice(range(10)) #range iterable bi komut oldugu icin bu sekilde de yazilabilir


# In[12]:


random.sample(range(10), k=4 ) #r 4 kere rastgele cikti aldi


# In[13]:


liste = [*range(10)]
print(liste)
random.shuffle(liste)
print(liste)


# In[14]:


import math


# In[15]:


help(math)


# In[16]:


math.ceil(7.1)


# In[17]:


round(7.1)


# In[18]:


math.floor(7.8)


# In[19]:


math.factorial(5)


# In[20]:


math.pow(3,2)

