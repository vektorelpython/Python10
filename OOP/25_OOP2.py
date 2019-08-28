
# class EvcilHayvan():
#     tur = ""
#     tuy_uzunlugu = ""  #instance
#     goz_rengi = ""
#     isim = ""
#     renk = ""

#     def besle(self):
#         print(self.isim,"beslendi")

# class Kopek(EvcilHayvan):
#     tur = "Köpek"
#     def odulMamasi():
#         print(self.isim,"Ödül Maması")
    
   

# class Kedi(EvcilHayvan):
#     tur = "Kedi"

# duman = Kedi()
# misket = Kedi()
# kara = Kopek()
# kara.isim = "Kara"
# misket.isim = "Misket"
# duman.tuy_uzunlugu = "kısa"
# misket.tuy_uzunlugu = "uzun"
# print(duman.tuy_uzunlugu)
# print(misket.tuy_uzunlugu)
# misket.besle()
# print(type(misket))




class Kopek():
    tur = "Kopek"
    def __init__(self,adi = "",tuy_uzunlugu = ""):
        self.adi = adi
        self.tuy_uzunlugu = tuy_uzunlugu
        self.besle()
    
    def besle(self):
        print(self.adi,"beslendi")
    
    def seslen(self):
        print(self.adi,"havladı")

    def odulMamasi(self):
        print(self.adi,"Ödül Maması")



class Kedi():
    tur = "Kedi"
    def __init__(self,adi = "",tuy_uzunlugu = ""):
        self.adi = adi
        self.tuy_uzunlugu = tuy_uzunlugu
        self.besle()
    
    def besle(self):
        print(self.adi,"beslendi")

    def seslen(self):
        print(self.adi,"miyavladı")

    def tuyKes(self):
        self.tuy_uzunlugu = "0"
        print(self.tuy_uzunlugu,self.adi,"temizlendi")


# print(dir(Kedi))
duman = Kedi("duman","kısa")
misket = Kedi("misket","uzun")
Kedi.tur = "asdasdasd"
print(misket.tur)
print(duman.tur)

misket.tuyKes()
print(duman.tuy_uzunlugu)