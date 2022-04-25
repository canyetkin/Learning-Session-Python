#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter
import random


# In[2]:


list1 = random.sample(range(10), k=4)
list2 = random.sample(range(10), k=4)
list3 = random.sample(range(10), k=4)
list4 = random.sample(range(10), k=4)

liste_listesi = [list1,list2,list3,list4]
liste_toplam = list1 + list2 + list3 + list4

print(liste_listesi)
print(liste_toplam)
      


# In[4]:


for index,liste in enumerate(liste_listesi):
    print("{}. liste \t {}".format(index+1,liste))


# In[5]:


Counter(liste_toplam)


# In[6]:


Counter("sldkfnlnfiafl")


# In[7]:


sarki = """Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev"""


# In[10]:


print(sarki)


# In[11]:


Counter(sarki)


# In[12]:


sarki.split()


# In[13]:


sarki.lower().split()


# In[14]:


Counter(sarki.lower().split())


# In[17]:


Counter(sarki.lower().split()).most_common(3)

