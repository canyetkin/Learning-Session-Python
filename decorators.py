#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### decorators


# In[ ]:


# degisken olarak fonksiyon


# In[1]:


def deneme():
    print("abc")


# In[8]:


f = deneme


# In[9]:


f()


# In[ ]:


# fonksiyon icinde fonksiyon 


# In[14]:


def deneme():
    print("deneme fonksiyonu calisiyor")
    def test():
        return "test fonksiyonu calisiyor"
    print(test())
    


# In[15]:


deneme() 


# In[27]:


def deneme():
    print("deneme fonksiyonu calisiyor")
    def test():
        return "test fonksiyonu calisiyor"
    return test


# In[22]:


deneme()


# In[32]:


f = deneme()


# In[33]:


f()


# In[34]:


f = deneme()
print(f())


# In[ ]:


### decorator ###


# In[44]:


def deneme():
    return "deneme fonksiyonu calisiyor"


# In[48]:


def ikinci(f):
    print("ikinci fonksiyon calisiyor")
    print(f())


# In[49]:


ikinci(deneme)


# In[50]:


def deco(f):
    def wrapper():
        print("baslangic")
        
        f()
        
        print("bitis")
        
    return wrapper


# In[51]:


def yazdir():
    print("can yetkin")


# In[52]:


def yazdir2():
    print("gokay demir")
    


# In[54]:


alt_fonksiyon = deco(yazdir)


# In[55]:


alt_fonksiyon()


# In[56]:


alt_fonksiyon2 = deco(yazdir2)


# In[57]:


alt_fonksiyon2()


# In[58]:


@deco
def yazdir():
    print("can yetkin")


# In[59]:


yazdir()


# In[60]:


@deco
def toplama(a,b):
    print(a+b)


# In[61]:


toplama(5,4)


# In[ ]:


"""
arguman alan fonksiyonlarda yukaridaki hatayi almanin sebebi,yukarida tanittigimiz wrapper
fonksiyonun bizde arguman bekliyor olması (  f() kismindan bahsediyorum )
"""


# In[ ]:


### arguman alan fonksiyonlarda docorator ###


# In[62]:


def deco(f):
    def wrapper(*args):
        print("baslangic")
        
        f(*args)
        
        print("bitis")
        
    return wrapper


# In[63]:


@deco
def toplama(a,b):
    print(a+b)


# In[64]:


toplama(5,4)


# In[ ]:


### arguman alan decoratorlar ###


# In[7]:


def deco(msg1,msg2):
    def ara_katman(f):
        def wrapper(*args):
            print(msg1)

            f(*args)

            print(msg2)

        return wrapper
    return ara_katman


# In[9]:


@deco("ilk","sonuc")
def toplama(a,b):
    print(a+b)


# In[10]:


toplama(5,4)


# In[29]:


import time
def sure_olc(f):
    def wrapper(*args):
        baslangic = time.time()
        print("Baslangic zamani: \t{}".format(baslangic))
        
        f(*args)
        
        bitis = time.time()
        print("Bitis zamani: \t{}".format(bitis))
        print("Gecen zaman: \t{}".format(bitis-baslangic))
    return wrapper


# In[36]:


@sure_olc
def faktoriyel(sayi):
    sonuc = 1
    while sayi > 1:
        sonuc = sonuc*sayi
        sayi -=1
    print(sonuc)


# In[49]:


faktoriyel(1)

