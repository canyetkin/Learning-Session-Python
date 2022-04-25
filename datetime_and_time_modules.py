#!/usr/bin/env python
# coding: utf-8

# In[21]:


import datetime


# In[14]:


from datetime import date


# In[ ]:


"""
datetime.date --------------------------

"""


# In[15]:


bugun = date.today()
print(bugun)


# In[16]:


dun = date(2022,4,24)
print(dun)


# In[17]:


bugun - dun


# In[22]:


yarin = bugun + datetime.timedelta(days=1)
print(yarin)


# In[24]:


zaman_araligi = yarin - dun
a = zaman_araligi.days
print(a)


# In[25]:


dun > bugun


# In[26]:


bugun.year


# In[27]:


bugun.month


# In[28]:


bugun.__getattribute__("month")


# In[ ]:


#ustteki iki yazim sekli de aynidir***


# In[29]:


date.isocalendar(bugun)


# In[ ]:


"""
normalde bugun.week gibi bi komut olmadigi icin hafta degerine ulasamiyoruz.
yukaridaki yazimla hafta sayisina ulasabiliriz, 2022 yilininn 17. haftasının 1. gunu anlamina 
gelir, ve normal indexlemeden farkli olarak saymaya 0 dan baslar. yani 1 = pazartesi
"""


# In[30]:


date.weekday(bugun)


# In[ ]:


"""
ustteki yazim sekli is date.isocalendar komutundan farkli olarak hafta gunlerini saymaya 
0 dan baslar, yani 0 = pazartesi
"""


# In[34]:


date.isocalendar(bugun)[0] #sonuc tuple oldugu icin [] ile parcalarina ulasabiliriz


# In[35]:


date.ctime(bugun)


# In[ ]:


# 'Mon Apr 25 00:00:00 2022' ciktisini verir, saat belirsiz cunku henuz tanimlamadik.


# In[ ]:


"""
datetime.time ----------------------------

"""


# In[36]:


from datetime import time


# In[37]:


zaman = time(21,15,6)
print(zaman)


# In[38]:


zaman.hour


# In[39]:


zaman.minute


# In[40]:


zaman.second


# In[ ]:


"""
datetime.datetime --------------------------
"""


# In[41]:


dt = datetime.datetime(2022,4,25,21,51,5)
print(dt)


# In[42]:


dt.month


# In[43]:


dt.hour


# In[ ]:


"""
time -----------------------
"""


# In[44]:


import time


# In[46]:


baslangic_zamani = time.time()
print("Baslama Zamani: \t{}".format(baslangic_zamani))
time.sleep(5)
bitis_zamani = time.time()
print("Bitis Zamani: \t{}".format(bitis_zamani))
print("Gecen sure : \t{}".format(round(bitis_zamani - baslangic_zamani)))

