#!/usr/bin/env python
# coding: utf-8

# ## Fonksiyon Uygulamasi

# ### Bilgi:
# 3 üzeri 2 = 9 
# Python'da üstel sayilari hesaplamak icin 3**2 seklinde gösterilir. 

# In[5]:


3**2


# #### Soru 1: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde doldurun

# In[3]:


def ustel_sayi_v1():
    """
    parametre: a: taban sayisi  b: kuvvet (üs) sayisi
    tip:       a: integer       b: integer
    örnek:     a: 3             b: 2
    
    r-return:  a üzeri b matematik isleminin sonucu
    r-tip:     integer
    r-örnek:   9
    """
    
    pass


# In[5]:


def ustel_sayi_v1(a,b):
    taban_sayisi = a
    kuvvet_sayisi = b
    c= a**b
    return("{} üzeri {} isleminin sonucu --> {}".format(a,b,c))
    
    


# In[7]:


ustel_sayi_v1(2,5)


# #### Soru 2: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde  ve  ** yerine for döngüsü ile hesaplayacak bicimde olusturun

# In[3]:


def ustel_sayi_v2(a,b):
    taban_sayisi = a
    kuvvet_sayisi = b
    sonuc = 1
    for x in range(b):
        sonuc=sonuc*a
    return sonuc
        


# In[4]:


ustel_sayi_v2(2,2)


# ### Bilgi:
# .sort() komutu listeyi kücükten büyüge siralar

# In[7]:


liste = [1,5,2,3,4]
liste.sort()
liste


# #### Soru 3: Asagidaki fonskiyonu 1 parametre alacak (sadece sayilardan olusan liste tipinde) ve en büyük iki sayiyi döndürecek bicimde olusturun

# In[20]:


def listedeki_en_buyuk_iki_sayi(*args):
    liste = list(args)
    liste.sort()
    a = liste[-1]
    b = liste[-2]
    return a,b


# In[22]:


def listedeki_en_buyuk_iki_sayiv2(liste):
    liste.sort()
    return liste[-1],liste[-2]


# In[23]:


deneme = [12,1,34,12,5]
listedeki_en_buyuk_iki_sayiv2(deneme)


# In[21]:


listedeki_en_buyuk_iki_sayi(2,3,4,5,6,345,342,65,234)


# ## Map, Filter ve Lambda Uygulamalari

# #### Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde) ve sadece str tipindeki degerleri filter ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun

# In[50]:


def str_filtrele(liste):
    print(list(filter(lambda x : x if type(x) == str else None, liste)))


# In[52]:


deneme =["a","b",True,False,1,3,4]
str_filtrele(deneme)


# #### Soru 5: Asagidaki fonskiyonu 1 parametre alacak (sadece sayi iceren liste tipinde) ve map ve lambda ifadelerini kullanarak 6 sifir atacak bicimde olusturun

# In[64]:


def paradan_alti_sifir_at(liste):
    sonuc=[]
    for x in liste:
        sonuc.append(int(x/1000000))
    return sonuc
    


# In[69]:


deneme = [1000000, 90000000, 15000000]
paradan_alti_sifir_at(deneme)


# In[75]:


def paradan_alti_sifir_at_v2(liste):
    return [*(map(lambda x : int(x/1000000,),liste))]
    


# In[76]:


paradan_alti_sifir_at_v2(deneme)


# ## Kullanici Girdisi Uygulamasi

# #### Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat ve dakika alacak bicimde olusuturun.

# In[1]:


def zaman_verisi_al():
    saat= input("Saat bilgisi giriniz: ")
    if saat.isdigit():
        saat = int(saat)
        if ((saat >= 0) and (saat < 24)):
            dakika = input("Dakika bilgisi giriniz: ")
            if dakika.isdigit():
                dakika = int(dakika)
                if ((dakika >= 0) and (dakika < 60)):
                    return("Saat {}:{}".format(saat,dakika))
                else:
                    return("Girdiginiz dakika degeri dakika araligina uymuyor")
            else:
                return("girdiginiz deger sayi tipinde degildir")  
        else:
            return("Girdiginiz saat degeri saat araligina uymuyor")  
    else:
        return("Girdiginiz deger sayi tipinde degildir")


# In[5]:


zaman_verisi_al()

