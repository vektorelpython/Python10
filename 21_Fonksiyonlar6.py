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
dosya = open(r"deneme.csv","r+")
print(dosya.read(18))
print(dosya.tell())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
dosya.seek(0)
liste = dosya.readlines()
print(liste)