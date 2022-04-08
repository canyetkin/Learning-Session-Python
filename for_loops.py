#!/usr/bin/env python
# coding: utf-8

# In[7]:


yorum_birakanlar = ["Ismail Aydemir", "Uygar Aydin", "Naz Yagcioglu","Ferhat Ibrik","Ulas Acil", "Bilal Kurucay"]


# In[8]:


for kullanici in yorum_birakanlar:
    print(kullanici)


# In[13]:


kullanici_sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_sayisi += 1
    print(kullanici_sayisi, kullanici)


# In[16]:


yorum_birakanlar[0].split()


# In[22]:


ad, soyad = yorum_birakanlar[0].split()[0], yorum_birakanlar[0].split()[1]
print(ad)
print(soyad)


# In[25]:


kullanici_sayisi = 0
for kullanıcı in yorum_birakanlar:
    kullanici_sayisi += 1
    ad = kullanıcı.split()[0]
    soyad = kullanıcı.split()[1]
    print("{}. kullacının adı {} ve soyadi {}".format(kullanici_sayisi, ad, soyad))


# In[27]:


liste2 = ["Harun Kocamemik","Can Yetkin","Baran Durman","Berat Onat","Sinan Kırcan","Yalcın Ucar"]
kullanıcı_sayısı = 0
oda_sahibi_sayısı = 0
for kullanıcı in liste2:
    if kullanıcı == "Can Yetkin":
        oda_sahibi_sayısı += 1
        ad = kullanıcı.split()[0]
        soyad = kullanıcı.split()[1]
        print("{}. oda sahibi adı {} ve soyadı {}".format(oda_sahibi_sayısı, ad, soyad))
    else: 
        kullanıcı_sayısı += 1
        ad = kullanıcı.split()[0]
        soyad = kullanıcı.split()[1]
        print("{}. oda sakini ismi {} ve soyadı {}".format(kullanıcı_sayısı, ad, soyad))


# In[1]:


tup1 = (1,2,3,4)
for sayi in tup1:
    print(sayi)


# In[3]:


liste3 = [[0,1],[2,3],[4,5]]
for x in liste3:
    print(x)


# In[10]:


liste3 = [[0,1],[2,3],[4,5]]
for x,y in liste3:
    print(x*y)


# In[21]:


dict1 = {
    "ad": "Can",
    "soyad": "Yetkin"
}
for k,v in dict1.items():
    print("Key: {} \t  Value: {}".format(k,v))

