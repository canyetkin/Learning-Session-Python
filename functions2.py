#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

map , filter and lambda expressions

"""


# In[1]:


def karesini_al(x):
    return x**2


# In[2]:


karesini_al(5)


# In[20]:


sayilar = [*range(1,6)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])
print(sayilar)
    
    
    
    


# In[22]:


"""
yukarıdaki kodu anlayabilmek icin acıklama: range(len(sayilar))) komutuyla listenin 0. 
indexinden itibaren son indexine kadar sırayla tanıttıgımız index degiskenine atadık.

"""


# In[34]:


sayilar = [*range(1,6)]
list(range(len(sayilar)))


# In[42]:


sayilar = [*range(1,6)]
print(sayilar)
[*map(karesini_al,sayilar)]


# In[ ]:


"""
yukarıda goruldugu gibi, map komutu verdigimiz fonksiyonu yine verdigimiz listenin her 
elemanına uyguluyor.

"""


# In[46]:


def cift_sayi_filtrele(x):
    if x%2==0:
        return x
    else:
        return None


# In[ ]:


"""
yukarıdaki kodu aşağıdaki gibi de yazabiliriz

"""


# In[51]:


def cift_sayi_filtrelev2(x):
    return x if x%2==0 else None


# In[57]:


sayilar = [*range(1,6)]
[*filter(cift_sayi_filtrelev2,sayilar)]


# In[ ]:


"""
lambda uygulamaları
"""


# In[58]:


def karesini_al(x):
    return x**2


# In[60]:


sayilar = [*range(1,6)]
list(map(lambda x : x**2,sayilar))


# In[63]:


sayilar = [*range(1,6)]
list(filter(lambda x : x if x%2==0 else None, sayilar))

