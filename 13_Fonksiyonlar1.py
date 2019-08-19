# def merhaba(ad):
#     print("Merhaba",ad)

# def pi(basamak=4):
#     print(round(22/7,basamak))
# #
#
# adi =  input("Adınızı Giriniz")
# merhaba(adi)
# pi()

# def Toplafonk(param1,param2):
#     print(param1 + param2)
# def Carpfonk(param1,param2):
#     print(param1 * param2)
# def Bolfonk(param1,param2):
#     print(param1 / param2)

# def Cikarfonk(param1,param2):
#     print(param1 - param2)

import random
def cevirASCII(karakter):
    var1 = str(ord(karakter))
    while len(var1) % 3 > 0:
        var1 = "0" + var1
    return var1

def cevirKarakter(ASCII):
    return chr(ASCII)

def sifrele(metin):
    var1 = ""
    sayi = random.randint(0,999)
    sonuc = str(sayi)
    for kar in metin:
        sonuc += str(cevirASCII(kar))
    liste = []
    for i in range(0,int(len(sonuc)/3)):
        liste.append(sonuc[i*3:(i*3)+3])
    liste2 = liste[1:]
    liste2.reverse()
    for i in range(0,len(liste2)):
        liste2[i] = int(liste[0]) - int(liste2[i])
    liste2.insert(0,liste[0])
    return liste2

isim = input("şifreyi giriniz")
print(sifrele(isim))








