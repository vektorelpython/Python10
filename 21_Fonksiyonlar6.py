def dosyaAc(adres="defter.csv"):
    import os 
    if os.path.exists(adres):
        dosya = open(adres,"r+")
    else:
        dosya = open(adres,"w+")
    return dosya

def Listele():
    dosya = dosyaAc("deneme.csv")
    liste = dosya.readlines()
    for i in range(0,len(liste)):
        adi,soyadi,telefon = liste[i].split(";")
        metin = "{}-{} {} {}".format((i+1),adi,soyadi,telefon)
        print(metin)
    dosya.close()


def girisAl(**kwargs):
    sonuc = ""
    for key,value in kwargs.items():
        if key=="ALANLAR":
            for item in value:
                sonuc+= input(item + " giriniz ") + ";"
    sonuc = sonuc.rstrip(";") + "\n"
    return sonuc 

# def ekleme():
#     kayit = girisAl(ALANLAR=["Adı","Soyadı","Telefon"])
#     dosya = dosyaAc("deneme.csv")
#     liste =  dosya.readlines()
#     liste.insert(0,kayit)
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


def arama():
    pass

# def silme():
#     Listele()
#     kayitID = int(input("Düzenlenecek Kaydı Seç"))
#     dosya = dosyaAc("deneme.csv")
#     liste = dosya.readlines()
#     liste.pop(kayitID-1)
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()
#     Listele()

# def duzeltme():
#     Listele()
#     
#     dosya = dosyaAc("deneme.csv")
#     liste = dosya.readlines()
#     kayit = girisAl(ALANLAR=["Adı","Soyadı","Telefon"])
#     liste[kayitID-1] = kayit
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


def idu(param=0):
    Listele()
    kayit = ""
    dosya = dosyaAc("deneme.csv")
    liste = dosya.readlines()
    # ekleme
    if param == 1:
        kayit = girisAl(ALANLAR=["Adı","Soyadı","Telefon"])
        liste.insert(0,kayit)
    #düzeltme
    elif param == 2:
        kayitID = int(input("Düzenlenecek Kaydı Seç"))
        kayit = girisAl(ALANLAR=["Adı","Soyadı","Telefon"])
        liste[kayitID-1] = kayit
    #silme
    elif param==3:
        kayitID = int(input("Silinecek Kaydı Seç"))
        liste.pop(kayitID-1)
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()


menu = """
1-Ekleme
2-Düzeltme
3-Silme
4-Listeleme
5-Arama
6-Çıkış
"""
anahtar = 1
while anahtar == 1:
    print("*"*30)
    print(menu)
    print("*"*30)
    islem = int(input("İşlem Seçimi"))
    if islem in (1,2,3):
        idu(islem)
    elif islem == 4:
        Listele()
    elif islem == 5:
        arama()
    elif islem == 6:
        anahtar = 0
    else:
        print("Menü Dışında Seçenek Girdin ")
else:
    print("İyi Günler Dileriz")
    