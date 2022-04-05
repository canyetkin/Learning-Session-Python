#!/usr/bin/env python
# coding: utf-8

# In[25]:


#tuple
#tuple
#tuple


# In[26]:


liste = ["a","b","c","d","e","a"]
tup = ("a","b","c","d","e","a")


# In[6]:


print(liste[0])


# In[7]:


print(tup[0])


# In[8]:


liste[0] = 17
print(liste)


# In[10]:


tup[0] = 17
print(tup)


# In[12]:


tup.count("a")


# In[13]:


tup.count("b")


# In[15]:


print(tup)


# In[16]:


tup.count(True)


# In[22]:


tup.index("a")


# In[24]:


tup.index(True)


# In[ ]:


#dictionary
#dictionary
#dictionary


# In[56]:


dict1 = {'isim': 'Can', 'yas':20, 'lokasyon': 'Eskisehir'}
dict1


# In[60]:


dict2 = {
    "isim": "Can",
    "yas": 20,
    "dogdugu_sehir": "Ankara",
    "yasadıgı_sehir": "Eskisehir"
# "lokasyon": "eskisehir"
    
}
dict2


# In[61]:


dict3 = {
    "isim": "Can",
    "yas": 20,
    "lokasyon": {
        "dogdugu_sehir": "Ankara",
        "yasadıgı_sehir": "Eskisehir"
    }
    
}
dict3


# In[62]:


print(dict2["yas"])


# In[63]:


print(dict3["lokasyon"])


# In[64]:


print(dict3["lokasyon"]["yasadıgı_sehir"])


# In[65]:


print(dict3["lokasyon"]["dogdugu_sehir"])


# In[66]:


dict3.get("lokasyon")


# In[67]:


dict3.get("lokasyon").get("dogdugu_sehir")


# In[75]:


dict3.keys()


# In[73]:


dict3.values()


# In[76]:


dict3.items()

