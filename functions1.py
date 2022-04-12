#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bes_bastir():
    print(5)


# In[2]:


bes_bastir()


# In[3]:


def bes_dondur():
    return 5


# In[4]:


bes_dondur()


# In[6]:


a = bes_bastir()
print(a)


# In[7]:


b = bes_dondur()
b


# In[8]:


print(a)
print(b)


# In[9]:


def sayi_dondur(sayi):
    return sayi


# In[10]:


sayi_dondur(20)


# In[11]:


def buyuk_sayi_dondur(a,b):
    if a>b :
        return a
    elif a == b :
        return("sayilar esittir")
    else:
        return b
        
    


# In[13]:


buyuk_sayi_dondur(228,14)


# In[14]:


def sayii_dondur(sayi=250):
    return sayi


# In[16]:


sayii_dondur(20)


# In[17]:


sayii_dondur()


# In[19]:


buyuk_sayi_dondur(23,45)


# In[20]:


def metin_yazdir(a,b):
    buyuk_sayi = buyuk_sayi_dondur(a,b)
    print("{} daha buyuk sayidir".format(buyuk_sayi))


# In[21]:


metin_yazdir(13,12)


# In[41]:


def isim_soyisim_ayirma(ad_soyad):
    ad = ad_soyad.split()[0]
    soyad = ad_soyad.split()[1]
    return ad,soyad


# In[43]:


a,b = isim_soyisim_ayirma("can yetkin")
print(a)
print(b )


# In[45]:


a = " ".join(["can","yetkin"])


# In[46]:


a


# In[47]:


def isim_soyisim_birlestir(ad,soyad):
    return " ".join([ad,soyad])
    


# In[49]:


isim_soyisim_birlestir("ahmet","can","yetkin")


# In[ ]:


"""
    args argumanı
    args argumanı --->  *args olarak kullanılır
    fonksiyonun arguman kısmına sınırsız arguman verebilirsin bununla
    ve liste ozelligi tasır

"""


# In[52]:


def isim_soyisim_birlestirv2(*args):
    return " ".join(args)


# In[54]:


isim_soyisim_birlestirv2("ahmet","can","yetkin")


# In[58]:


"-".join(["can","yetkin"])


# In[ ]:


"""

**kwargs komutu ile dict olusturup farklı degiskenleri key-value standartında saklayabilirsin
**kwargs kommutu bir dictionary olusturdugu icin .get(), .keys, .items,values gibi kavramları
da kullanabilirsin

"""


# In[69]:


def gobek_adi_yazdiriciv2(**kwargs):
    if "gobekadi" in kwargs:
        print(kwargs.get("gobekadi"))
    else:
        print("gobekadi yok")


# In[70]:


gobek_adi_yazdiriciv2(ad = "Ahmet", gobekadi = "can", soyad = "Yetkin")


# In[ ]:




