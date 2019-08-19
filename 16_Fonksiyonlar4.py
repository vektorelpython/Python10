# a = 4
# def fonk():
#     global a
#     a = 8
#     print(a)
# fonk()
# print(a)


# dosya = open("deneme.csv","r+")
# Adi = input("Adınızı Giriniz")
# Soyadi = input("Soyadinizi Giriniz")
# Telefon = input("Telefonu Giriniz")
# kayit = "{};{};{}".format(Adi,Soyadi,Telefon)
# dosya.read()
# print(kayit)
# dosya.write(kayit)
# dosya.close()

# dosya = open("deneme.csv","r+")
# Adi = input("Adınızı Giriniz")
# Soyadi = input("Soyadinizi Giriniz")
# Telefon = input("Telefonu Giriniz")
# kayit = "\n{};{};{}".format(Adi,Soyadi,Telefon)
# liste = dosya.readlines()
# print(liste)
# liste.append(kayit)
# dosya.seek(0)
# dosya.truncate()
# dosya.writelines(liste)
# dosya.close()
     
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



Listele()
