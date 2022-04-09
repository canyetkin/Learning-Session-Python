#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=0
while x < 10:
    print("{} sayisi 10'dan kücüktür".format(x))
    x += 1


# In[4]:


x=0
while x < 10:
    print("{} sayisi 10'dan kücüktür".format(x))
    x += 1
else:
    print("{} sayisi 10'dan kücük degildir".format(x))


# In[ ]:


#faktoriyel ornegi


# In[20]:


sayi = 5
sonuc = 1
while sayi >0:
    sonuc = sayi * sonuc
    sayi -= 1
print(sonuc)


# In[2]:


range(10)


# In[3]:


list(range(10))


# In[7]:


liste1 = list(range(10))
print(liste1)


# In[8]:


[*range(10)] #bu kullanım ve list(range(10)) aynı şey


# In[9]:


liste2 = [*range(10)]
print(liste2)


# In[10]:


[*range(2,9,2)]


# In[22]:


for sayi in range(10):
    if sayi <= 5:
        if sayi < 5:
            print("sayi 5 den kucuktur")
        else:
            print("sayi 5 e esittir")
    else:
        print(sayi)


# In[28]:


harfler = ["a","b","c","d","e"]
for harf in enumerate(harfler):
   print(harf)


# In[32]:


harfler = ["a","b","c","d","e"]
for index,harf in enumerate(harfler):
   print("{} numaralı harf {}".format(index+1, harf))


# In[54]:


ulkeler = ["turkiye","almanya","fransa"]
siralamalar = list(range(1,4))
for  ulke in zip(ulkeler, siralamalar):
    ad = ulke[0]
    sıralama = ulke[1]
    print("{} isimli ülkenin sıralması {}".format(ad,sıralama))
    


# In[ ]:


#break
#continue
#pass


# In[57]:


harfler = ["a","b","c","d","e"]*100
for index,harf in enumerate(harfler):
    if harf == "c":
        print("{} harfi {}. indexte!!".format(harf,index))
        break
    


# In[62]:


for sayi in range(1,9):
    if sayi%2 == 0:
        continue
    print(sayi)


# In[76]:


for sayi in range(1,9):
    if sayi%2 == 0:
        pass
    print(sayi)

