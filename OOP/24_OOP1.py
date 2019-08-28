#Encapsulation
#Inheritance
#PolyMorphism
#Abstraction

class EvcilHayvan():
    tur = ""
    tuy_uzunlugu = ""  #instance
    goz_rengi = ""
    isim = ""
    renk = ""

    def besle(self):
        print(self.isim,"beslendi")

class Kopek(EvcilHayvan):
    tur = "Köpek"
    def odulMamasi():
        print(self.isim,"Ödül Maması")
    
   

class Kedi(EvcilHayvan):
    tur = "Kedi"
    


duman = Kedi()
duman.tur = "1"
misket = Kedi()
misket.tur = "2"
print(duman.tur)
print(misket.tur)
Kedi.tur = "3"
print(duman.tur)
print(misket.tur)


# kara = Kopek()
# kara.isim = "Kara"
# misket.isim = "Misket"
# duman.tuy_uzunlugu = "kısa"
# misket.tuy_uzunlugu = "uzun"
# print(duman.tuy_uzunlugu)
# print(misket.tuy_uzunlugu)
# misket.besle()
# print(type(misket))