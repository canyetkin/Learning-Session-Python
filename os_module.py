#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('ls', '')


# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[ ]:


"""
yukaridaki iki komut jupyter notebook' a ozel komutlar, baska operatorlerde calismaz, ayni 
islemi os modulu ile tum derleyicilerde yapabilirsin.
"""


# In[ ]:


"""

os modulu

"""


# In[ ]:


"""

navigasyon ve icerik listeleme

"""


# In[3]:


import os


# In[4]:


os.getcwd() #get current working directory


# In[5]:


os.listdir() 


# In[6]:


os.listdir('/Users/ahmetcanyetkin/Desktop')


# In[7]:


os.chdir('/Users/ahmetcanyetkin/Desktop')


# In[8]:


os.getcwd()


# In[9]:


os.listdir()


# In[11]:


dosyalar = os.listdir()
for eleman in dosyalar:
    print (eleman)


# In[ ]:


"""

yeni eleman olusturma,isim degistirme ve silme;;;;

"""


# In[13]:


os.mkdir('/Users/ahmetcanyetkin/Desktop/deneme') #mkdir means make directory 


# In[14]:


os.listdir()


# In[15]:


os.rmdir('/Users/ahmetcanyetkin/Desktop/deneme') #rmdir means romove directory


# In[16]:


os.listdir()


# In[ ]:


## os.O_RDONLY − Read Only      - Sadece Oku
## os.O_WRONLY − Write Only     - Sadece Yaz
## os.O_RDWR   − Read and Write - Oku ve Yaz
## os.O_CREAT  - Create         - Olustur


# In[17]:


yeni_dosya = os.open("yeni_dosya.txt",os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya, "Merhaba Dünya!")
os.close(yeni_dosya)
 


# In[ ]:


"""
yukaradaki yazimda strtipi yazi girdigim icin hata verdi, byte'a donusturmek icin 
asagıdaki gibi yazilabilir;

"""


# In[18]:


yeni_dosya = os.open("yeni_dosya.txt",os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya, "Merhaba Dünya!".encode())
os.close(yeni_dosya) 


# In[19]:


os.listdir()


# In[22]:


yeni_dosya = os.open("yeni_dosya.txt", os.O_RDONLY)
icerik = os.read(yeni_dosya,5)
os.close(yeni_dosya)
print(icerik)


# In[ ]:


"""
os.read() komutu iki adet argüman alir, ikincisi uzunluk, yukarida goruldugu gibi
verdigin deger kadar okuma yapar, asagıdaki gibi dinamik olarak da yazilabilir;;;

"""


# In[27]:


yeni_dosya = os.open("yeni_dosya.txt", os.O_RDONLY)
uzunluk = os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,uzunluk)
print(icerik.decode()) #bu satırda yukarıda encode komutuyla turkce karakterledi byte'a donusturmustuk,decode ile tekrar tam tersini  yaptik ve turkce karakterlere ulastik
os.close(yeni_dosya)


# In[ ]:


"""
dosya silme;;
(klasorleri os.rmdir(name) komutuyla, dosyaları os.unlink(name) komutuyla siliyoruz )

"""


# In[28]:


os.unlink("yeni_dosya.txt") #bunun sonucu olarak suan calismakta oldugum desktop klasorunden istedigim dosyayi sildi..


# In[ ]:


"""
mevcut dosyanin ismini degistirme;;;
"""


# In[30]:


os.getcwd()


# In[31]:


os.mkdir("deneme_yeni")


# In[33]:


os.listdir()


# In[34]:


os.rename("deneme_yeni","deneme_eski")


# In[35]:


os.listdir()


# In[36]:


os.rmdir("deneme_eski")


# In[39]:


os.listdir()

