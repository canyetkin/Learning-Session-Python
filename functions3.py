#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
input ile kullanıcı girdisi almak
"""


# In[1]:


input("bir sayi girin:")


# In[2]:


a = input("bir sayi girin:")
type(a)


# In[5]:


a = input("bir sayi girin:")
type(int(a)) 


# In[8]:


def uygulama():
    sayi = input("bir sayi giriniz: ")
    cevap = input("sayi tek mi cift mi: ")
    if cevap == "cift":
        if int(sayi)%2==0:
            print("dogru! {} sayisi bir cift sayidir".format(sayi))
        else:
            print("yanlıs!! {} sayisi bir tek sayidir".format(sayi))
    elif cevap == "tek":
        if int(sayi)%2==1:
            print("dogru!! {} sayisi bir tek sayidir".format(sayi))
        else:
            print("yanlıs!! {} sayisi bir cift sayidir".format(sayi))


# In[10]:


uygulama()


# In[ ]:


"""

kullanıcı girdisini onaylamak 

"""


# In[1]:


def sayi_girdisi_kontrol():
      girdi = input("bir sayi giriniz: ")
      deneme_hakki = 3
      
      while not girdi.isdigit():
          if deneme_hakki > 0 :
              deneme_hakki -= 1
              print("Girdiginiz deger bir sayi degildir! Tekrar deneyin")
              print("kalan deneme hakkı ---> {}".format(deneme_hakki))
              girdi = input("bir sayi giriniz: ")
          else:
              print("deneme hakkiniz kalmadi!")
              break
      else:
          print("tebrikler, girdiginiz deger bir sayidir!")
              


# In[3]:


sayi_girdisi_kontrol()


# In[6]:


def eposta_kontrol():
    girdi = input("Gecerli bir eposta adresi giriniz: ")
    while not (("@"in girdi) and ("."in girdi)):
            print("hatalı giris yaptiniz")
            girdi = input("Gecerli bir eposta adresi giriniz: ")
    else:
        print("Tebrikler basarıyla giris yaptınız!")
    


# In[9]:


eposta_kontrol()


# In[ ]:


"""

try,expect ve finally komutlarıyla hata tedbiri

"""


# In[ ]:


"""
round() komutu ile tamsayıya yuvarlama yapılır.
"""


# In[10]:


def tam_sayiya_cevir():
    girdi = input("Bir ondalık sayı giriniz: ")
    print(round(float(girdi)))


# In[11]:


tam_sayiya_cevir()


# In[12]:


tam_sayiya_cevir()


# In[27]:


def tam_sayiya_cevir():
    girdi = input("Bir ondalık sayı giriniz: ")
    try:
        girdi = float(girdi)
        print(round(girdi))
    except:
        print("Girdiginiz '{}' degeri tam sayiya cevirilemiyor.".format(girdi))


# In[29]:


tam_sayiya_cevir()


# In[30]:


def tam_sayiya_cevir():
    girdi = input("Bir ondalık sayı giriniz: ")
    try:
        girdi = float(girdi)
    except:
        print("Girdiginiz '{}' degeri tam sayiya cevirilemiyor.".format(girdi))
    else: 
        print("yuvarlama isleminin sonucu {}".format(round(girdi)))


# In[32]:


tam_sayiya_cevir()


# In[40]:


def tam_sayiya_cevir():
    girdi = input("Bir ondalik sayi giriniz: ")
    status = ""
    try:
        girdi = float(girdi)
        print("Yuvarlama isleminin sonucu {} ".format(round(girdi)))
        status = "basarili"
    except:
        print("Girdiginiz ''{}'' degeri tam sayiya cevirilemiyor".format(girdi))
        status = "basarisiz"
    finally:
        print("Tam sayiya yuvarlama islemi {} olarak tamamlandı.".format(status))


# In[41]:


tam_sayiya_cevir()


# In[42]:


tam_sayiya_cevir()


# In[43]:


def tam_sayiya_cevir_dongu():
    girdi = input("Bir ondalık sayi giriniz")
    
    while True:
        try:
            girdi = float(girdi)
            print("Yuvarlama isleminin sonucu {} ".format(round(girdi)))
            break
        except:
            print("Girdiginiz deger tamsayiya cevrilemiyor, tekrar deneyiniz")
            girdi = input("Bir ondalık sayi giriniz")
        
            


# In[44]:


tam_sayiya_cevir_dongu()


# In[ ]:


"""

exception tipleri

"""


# In[46]:


5 + "a"


# In[47]:


try:
    5 + "a"
except TypeError:
    print("girdiginiz verilerle islem yapilamiyor")
except:
    print("bu kod düzgün calismiyor")


# In[48]:


try:
    5 + "a"
except IndexError:
    print("girdiginiz verilerle islem yapilamiyor")
except:
    print("bu kod düzgün calismiyor")


# In[53]:


liste = []

try:
    liste[-1]
except IndexError:
    print('Indexlemeye calistiginiz eleman listenin disinda')
except: 
    print('kod duzgun calismiyor')


# In[75]:


vatandas = {
    "AD" : "Can",
    "TC_NO" : "123123123"
}
try:
    print(vatandas['PASS_NO'])
except IndexError:
    print('Indexlemeye calistiginiz eleman listenin disinda')
except KeyError:
    print("girdiginiz key degeri dictionaryde bulunamadı")
except : 
    print('kod duzgun calismiyor')

