class EvcilHayvan():
    tur = ""
    def __init__(self,adi = "",tuy_uzunlugu = ""):
        self.adi = adi
        self.tuy_uzunlugu = tuy_uzunlugu
        self.besle()
    
    def seslen(self):
        print(self.adi,"ses çıkardı")

    def besle(self):
        print(self.adi,"beslendi")


class Kopek(EvcilHayvan):
    tur = "Kopek"
    def __init__(self,adi = "",tuy_uzunlugu = ""):
        super().__init__(adi,tuy_uzunlugu)
        

    def seslen(self):
        print(self.adi,"havladı")

    def odulMamasi(self):
        print(self.adi,"Ödül Maması")



class Kedi(EvcilHayvan):
    tur = "Kedi"
    def __init__(self,adi = "",tuy_uzunlugu = ""):
        super().__init__(adi,tuy_uzunlugu)
    
    def seslen(self):
        print(self.adi,"miyavladı")

    def tuyKes(self):
        self.tuy_uzunlugu = "0"
        print(self.tuy_uzunlugu,self.adi,"temizlendi")


class Kus(EvcilHayvan):
    tur="Kus"
    def __init__(self,adi = "",tuy_uzunlugu = "",tuy_rengi=""):
        super().__init__(adi,tuy_uzunlugu)
        self.tuyrengi = tuy_rengi

    def Uc(self):
        print(self.adi,"uçtu")


misket = Kedi("misket","kısa")
duman = Kedi("duman","uzun")
kara = Kopek("kara")
hayko = Kopek("hayko")
misket.seslen()
hayko.seslen()
maviş = Kus("Maviş","Uzun","Renkli")

