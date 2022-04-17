#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Ucus():
    havayolu = "TYH"


# In[2]:


ucus1 = Ucus()


# In[3]:


ucus1.havayolu


# In[4]:


class Ucus():
    havayolu = "TYH"
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis 
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        


# In[5]:


ucus2 = Ucus()


# In[7]:


ucus2 = Ucus("TK123", "ANK", "IST", 50, 300, 250)


# In[8]:


ucus2.varis


# In[9]:


ucus2.kalkis


# In[10]:


ucus2.sure


# In[11]:


ucus2.havayolu


# In[12]:


ucus3 = Ucus('TK223', 'BOD', 'ANT', 40, 250, 250)


# In[14]:


ucus3.havayolu


# In[2]:


class Ucus():
    havayolu = "TYH"
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis 
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        
    def anons_yap(self):
        return "{} sayili {}-{} ucusumuz {} dakika surecektir".format(
        self.kod,
        self.kalkis,
        self.varis,
        self.sure)
    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu 
    
    def bilet_satis(self,bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print("{} adet bilet satilmistir, kalan bos koltuk sayisi {}".format(
                 bilet_adedi,
                 self.koltuk_sayisi_guncelle()))
            
        else:
            print("Islem gerceklestirilemedi, yetersiz koltuk sayisi..")
            
    def bilet_iptal(self,iptal_adedi=1):
        if iptal_adedi <= self.yolcu:
            self.yolcu -= iptal_adedi
            print("{} adet bilet iptal edilmistir, guncel bos koltuk sayisi {}".format(
            iptal_adedi,
            self.koltuk_sayisi_guncelle()))
            
        
    
        


# In[3]:


ucus3 = Ucus('TK223', 'BOD', 'ANT', 40, 250, 25)


# In[ ]:


"""
double under score (dunder) methods

"""


# In[12]:


class Ucus():
    havayolu = "TYH"
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis 
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        
    def __repr__(self):
        return("{} kodlu ucus sisteme tanimlanmistir".format(self.kod))
        
    def anons_yap(self):
        return "{} sayili {}-{} ucusumuz {} dakika surecektir".format(
        self.kod,
        self.kalkis,
        self.varis,
        self.sure)
    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu 
    
    def bilet_satis(self,bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print("{} adet bilet satilmistir, kalan bos koltuk sayisi {}".format(
                 bilet_adedi,
                 self.koltuk_sayisi_guncelle()))
            
        else:
            print("Islem gerceklestirilemedi, yetersiz koltuk sayisi..")
            
    def bilet_iptal(self,iptal_adedi=1):
        if iptal_adedi <= self.yolcu:
            self.yolcu -= iptal_adedi
            print("{} adet bilet iptal edilmistir, guncel bos koltuk sayisi {}".format(
            iptal_adedi,
            self.koltuk_sayisi_guncelle()))
            
        else:
            return "iptal edilmek istenen bilet adedi mevcut degil"
            
        
            
        
    
        


# In[13]:


ucus3 = Ucus('TK223', 'BOD', 'ANT', 40, 250, 25)


# In[15]:


ucus3.__dir__()


# In[ ]:


"""

inheritance 

"""


# In[16]:


class Seyahat():
    
    def __init__(self,kalkis,varis):
        self.kalkis = kalkis
        self.varis = varis
    def anons(self):
        return "{}-{} seyahatine hosgeldiniz".format(self.kalkis,self.varis)
class Otobus(Seyahat):
    
    def __init__(self,mola_duraklari,kalkis,varis):
        Seyahat.__init__(self,kalkis,varis)
        self.mola_duraklari = mola_duraklari
        
        
    
        


# In[17]:


seyahat1 = Seyahat("ANT","BOD")


# In[18]:


seyahat1.kalkis


# In[19]:


seyahat1.varis


# In[20]:


otob1 = Otobus(["FET","ALAN"], "ANT", "BOD")


# In[22]:


otob1.mola_duraklari

