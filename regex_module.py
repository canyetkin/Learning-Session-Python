#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
REgular expressions, REGEX module
"""


# In[1]:


import re


# In[2]:


cumle = "Mustafa Kemal Ataturk, Turk asker, devlet adami ve Turkiye Cumhuriyeti'nin kurucusudur"

patern = "Turk"

re.search(patern,cumle)


# In[ ]:


#yukarıdaki re.search komutu sadece ilk eslesmeyi bulur ve durur, ve str tipinde cikti verir.


# In[3]:


durum = re.search(patern,cumle)
durum.span()


# In[ ]:


#buldugu match sonucu bir obje oldugu icin class komutlarini da kullanabilirirz;;;


# In[6]:


dir(durum)


# In[8]:


durum.start()


# In[9]:


durum.end()


# In[10]:


durum.group()


# In[ ]:


"""
coklu eslesmeler, match
"""


# In[21]:


for eslesme in re.findall(patern,cumle):
    print(eslesme)


# In[ ]:


# re.findall() komutu ile yine str buluruz ama bu sefer butun eslesmeleri dondurebilir 
# re.search() komutunu for dongusu icinde kullanamayiz cunku iterable degil


# In[23]:


for eslesme in re.finditer(patern,cumle):
    print(eslesme.span() , eslesme.group())


# In[ ]:


# re.finditer() komutuyla yukaridaki sekildeki gibi bi yazim yapabiliriz.
# fakat aynisini re.findall() komutyla yapamayiz cunku bu  komut str sonuc dondurur ve 
# str sonuc ustunde eslesme.span() , eslesme.group() gibi komutlari kullanamayiz.


# In[ ]:


"""
dinamik kullanim

"""


# In[ ]:


###############################################################################
####### Ifade ########## Aciklama ######## Örnek ########### Patern ###########
####### --------------------------------------------------------------- #######
#######  \d   #########   rakam  #######  base42  #########  base\d\d #########
#######  \w   ########   karakter  #####   R2-D2  ######### \w\w\w\w\w ########
#######  \s   ########    bosluk  ###### Ping Pong ######## Ping\sPong ########
#######  \D   #######   rakam degil  #####  base  #########  \D\D\D\D #########
#######  \W   #####   karakter degil  ###   R2D2  ######### \W\W\W\W ##########
#######  \S   #####    bosluk degil ##### PingPong ### \S\S\S\S\S\S\S\S #######
####### --------------------------------------------------------------- #######
###############################################################################


# In[25]:


ornek = "En sevdigim kanal base42"
patern=  r"base\d\d"
re.search(patern,ornek)


# In[33]:


cumle = "Selam, benim telefon numaram 0535-8886622."
patern = "\d\d\d\d-\d\d\d\d\d\d\d"
telnoobj = re.search(patern,cumle)


# In[35]:


tel_no = telnoobj.group()
print(tel_no)


# In[44]:


ornek = "Ping Pong oynamayi cok severim, ve de pata kute"
patern = r"\w\w\w\w\s\w\w\w\w"
re.findall(patern,ornek)


# In[ ]:


# string olarak patern tanitirken quote isaretinin disina r harfi koyulmasi onerilir.


# In[65]:


ornek = "Ping Pong oynamayi cok severim,"
patern = r"\w\w\w\w\s\w\w\w\w"
for match in re.findall(patern,ornek):
    if match == "Ping Pong":
        print(match)


# In[64]:


ornek = "Ping Pong oynamayi cok severim,"
patern = r"\w\w\w\w\s\w\w\w\w"
for eslesme in re.finditer(patern,ornek):
    print(eslesme)


# In[ ]:


######## Ifade ####### Aciklama ######## Örnek ############# Patern ############
####### ---------------------------------------------------------------- #######
#######  {5}   ########  adet  #######  aaaaa  #########    \w{5}     ##########
#######  {3,4} #######   veya  #######   abc  ##########   \w{3,4}     #########
#######  {2,}  ########  en az  ##### 198721321 ########    \d{2,}     #########
#######    *   ###  0 ya da fazla #######  x  ##########     \w*        ########
#######    +   ### 1 ya da fazla ######  Ahmet1  #######    \w+\d+     #########
#######    ?   #####  ya 1 ya hic ####### Mura #########     Murat?       ######
####### --------------------------------------------------------------- ########
################################################################################


# In[70]:


cumle = "Selam, benim telefon numaram 0535-8886622."
patern = r"\d{3,4}-\d{7}"

tel_no = re.search(patern, cumle).group()
print(tel_no)


# In[71]:


cumle = "En sevdigim kanal base42."
patern = r"\s\w{5,}"

for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())


# In[72]:


patern = r"\d?"

for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())


# In[ ]:


"""
yukaridaki ornekte soru isareti hem 0 hem 1 i karşilar, yani hem var hem yok, cumle 
degiskenindeki tum karakterler bu duruma uydugu ıcın tumunun indexi cikti olarak verildi.

"""


# In[76]:


cumle = "En sevdigim kanal base42."
patern = r"\d+"
for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())


# In[86]:


cumle = "En sevdigim kanal base42."
patern = r"\w*\d+"  # bu paterndeki yildiz isareti var ya da yok anlamina gelir.
for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())


# In[ ]:


#yukaridaki kodun ciktisi: base42
# * isareti 0 ya da daha fazla anlamina gelir


# In[81]:


cumle = "En sevdigim kanal 42base."
patern = r"\w*\d+"

for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())
    
    """
    bu kodun ciktisi "42", bu da patern siralamasinin onemli oldugunun bir ornegi
    """


# In[98]:


## GSM Operatörleri:
# 54...         -> Vodafone
# 501,505,506   -> AVEA
# 53...         -> Turkcell

def gsm_operator_bul():
    tel_no = input("telefon numaranizi giriniz :  ")
    patern = r"(\d{3})-(\d{7})"
    eslesme = re.search(patern,tel_no)
    if eslesme:
        gsm_kod = eslesme.groups()[0]
        if gsm_kod.startswith("54"):
            print("Vodafone")
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506"):
            print("Turk Telekom")
        elif gsm_kod.startswith("53"):
            print("Turkcell")
        else:
            print("sebeke bulunamadi")
        
    else:
        print("eslesme bulunamadi")


# In[100]:


gsm_operator_bul()


# In[ ]:


"""
yukaridaki fonksiyonu olustururken kullandigimiz paternde parantez kullanmamizin sebebi
sadece ilk kod kısmına ulasmak istememiz.
parantezle 2 farkli grup olsuturduk ve ardindan once re.search(patern,tel_no) komutuyla 
eslesmeye ulastik, sonra eslesme.groups()[0] komutuyla gruplardan ilkine yani gsm kodu kismina
ulastik.

if eslesme: diyip devam edebildilk, eslesme var ise anlamina geliyor.


.startswith("x") komutunu stringlerde kullanabiliriz.

"""


# In[ ]:


######## Ifade ####### Aciklama ######## Örnek ############# Patern ############
####### ---------------------------------------------------------------- #######
#######    |   ########  veya  #######  slm  #########    selam|slm   ##########
#######    ^    ####### baslar  #######  Ahmet  ##########   ^\w+      #########
#######    $   ########  biter   ##### base42   ########     \d$       #########
#######    .   ######  herhangi  #####  abcdef  ########      .*       #########
#######    \   ########  esc     #####  (not)   ########   \(\w{3}\)   #########
####### --------------------------------------------------------------- ########
################################################################################


# In[101]:


import re

def mesaj_hissi_bul(mesaj):
    hisler = []
    
    pozitif_patern = r"(merhaba|selam|ask|sevgi|dost|kardes|:\)+)"
    negatif_patern = r"(lan|aptal|abv|yeter|birak)"
    
    heyecanli_patern = r"!|[!|?]{2,}$"
    sakin_patern = r"^[Tabi+|Hayhay]"
    
    emin_patern = r"[K|k]esin|[T|t]abi|[E|e]lbet"
    kararsiz_patern = r"[B|b]elki|[S|s]anirim"
    
    if re.search(pozitif_patern, mesaj):
        hisler.append("Pozitif")
    if re.search(negatif_patern, mesaj):
        hisler.append("Negatif")
    if re.search(heyecanli_patern, mesaj):
        hisler.append("Heyecanli")
    if re.search(sakin_patern, mesaj):
        hisler.append("Sakin")
    if re.search(emin_patern, mesaj):
        hisler.append("Emin")
    if re.search(kararsiz_patern, mesaj):
        hisler.append("Kararsiz")
    
    return hisler


# In[102]:


cumle1 = "Naber abi? :)             "
cumle2 = "Tabiii ki buyrun          "
cumle3 = "Sacmalamayi birak artik!  "
cumle4 = "Belki yarindan da yakin..."
cumle5 = "Elbet birgün bulusacagiz  "
cumleler = [cumle1, cumle2, cumle3, cumle4, cumle5]
for cumle in cumleler :
    print(cumle, '\t', mesaj_hissi_bul(cumle))


# In[ ]:


"""
yukaridaki kodun ciktisi;

Naber abi? :)              	 ['Pozitif']
Tabiii ki buyrun           	 ['Sakin', 'Emin']
Sacmalamayi birak artik!   	 ['Negatif', 'Heyecanli']
Belki yarindan da yakin... 	 ['Kararsiz']
Elbet birgün bulusacagiz   	 ['Emin']

"""

