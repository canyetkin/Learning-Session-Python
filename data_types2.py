#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = True
b = False 
print(a)
print (b)
c = "True"
print(c)
print(type(c), type(a))
#class 'True' is different from True. True one is boolean, "True one  is string"


# In[6]:


yas1 = 20
yas2 = 18

print (yas1 > 18)
print (yas1 < 18)


# In[8]:


print(yas1 == 18)
print(yas2 == 18)


# In[15]:


print(yas1 != 18)
print(not yas1 == 18 )


# In[16]:


not yas2 < 18


# In[ ]:


#LISTS
#LISTS


# In[2]:


liste = ["a","b","c","d","e","a"]
print(liste)


# In[8]:


print(liste)


# In[10]:


print(liste[3:5])


# In[11]:


liste.append("g")


# In[12]:


print(liste)


# In[13]:


liste.pop()


# In[14]:


print(liste)


# In[18]:


liste.pop(5)


# In[19]:


print(liste)


# In[23]:


liste.pop()
print(liste)


# In[25]:


liste.append("d")


# In[27]:


print(liste)


# In[31]:


sayilar = [83547,2389,44,987,12,3,3,1]
sayilar.sort()
print(sayilar)


# In[33]:


sayilar.reverse()
print(sayilar)


# In[35]:


set(sayilar)


# In[36]:


print(sayilar)


# In[38]:


sayilar = set(sayilar)
print(sayilar)

