#!/usr/bin/env python
# coding: utf-8

# In[2]:


hava_durumu = "yagisli"
if hava_durumu == "yagisli":
    print("semsiyeni al!!")


# In[4]:


hava_durumu = "gunesli"
if hava_durumu == "yagisli":
    print("semsiyeni al!!")
else:
    print("sikinti yok..")


# In[7]:


hava_durumu = "yagisli"
if hava_durumu == "yagisli":
    print("semsiyeni al!!")
elif hava_durumu == "karli":
    print("atkını al")
else:
    print("sikinti yok..")


# In[11]:


yas = 14
if yas > 18:
    print("hosgeldiniz!!")
else:
    print("sana burda yer yok bebek")


# In[44]:


liste = ["a","b","c"]


# In[57]:


hedef_harf = "x"
if hedef_harf in liste:
    print("buldum")
else:
    liste.append(hedef_harf)
    print("bulamadım ve ekledim")
    print("güncel liste:{}".format(liste))
    
    


# In[75]:


hedef_harf = "h"
if (hedef_harf in liste) and (hedef_harf == liste[0]):
    print("buldum ve ilk konumda")
elif hedef_harf in liste:
    print("buldum ama ilk konumda degil")
    print("harf konumu: {}".format(liste.index(hedef_harf)))
else:
    liste.append(hedef_harf)
    print("bulamadım ve ekledim")
    print("güncel liste:{}".format(liste))
    
    


# In[76]:


liste

