
def Toplafonk(param1,param2):
    return param1 + param2
def Carpfonk(param1,param2):
    return param1-param2
def Bolfonk(param1,param2):
    if param2 != 0:
        return param1 / param2
    else:
        return -1
def Cikarfonk(param1,param2):
    return param1 - param2

def kuvvetAlma(param1,param2):
    return param1**param2
def kokAlma(param1,param2):
    return param1**(1/2)

def faktoriyel(param1,param2):
    sonuc = 1
    for i in range(1,param1+1):
        sonuc *= i
    return sonuc

def islemCagir(fonk,islem):
    param2 = 0
    param1 = int(input("1. Sayıyı Gir"))
    if islem not in (6,5):
        param2 = int(input("2. Sayıyı Gir"))

    return fonk(param1,param2)

def AnaMenu():
    islemMenu = """
    1-Topla
    2-Çıkar
    3-Böl
    4-Çarp
    5-Faktoriyel
    6-Kök Alma
    7-Kuvvet Alma
    8-Çıkış
    """
    while True:
        print(islemMenu)
        sonuc = ""
        islem = int(input("islem numarasını giriniz"))
        if islem == 1:
            sonuc = islemCagir(Toplafonk,islem)
        elif islem == 2:
            sonuc = islemCagir(Cikarfonk,islem)
        elif islem == 3:
            sonuc = islemCagir(Carpfonk,islem)
        elif islem == 4:
            sonuc = islemCagir(Bolfonk,islem)
        elif islem == 5:
            sonuc = islemCagir(faktoriyel,islem)
        elif islem == 6:
            sonuc = islemCagir(kokAlma,islem)
        elif islem == 7:
            sonuc = islemCagir(kuvvetAlma,islem)
        elif islem == 8:
            break
        print(sonuc)
AnaMenu()