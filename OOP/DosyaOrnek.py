from OOP.DosyaUtility import DosyaTool as Dt
from datetime import datetime as dt
class OtelMusteri():
    __otelisim = "Turist"
    def __init__(self,*args,**kwargs):
        self.musSoyad = ""
        self.musTel = ""
        self.Oda = ""
        self.GunSay = ""
        self.Bas ="111"
        for key,value in kwargs.items():
            if key == "Ad":
                self.musAd = value
            elif key == "Soyad":
                self.musSoyad = value
            elif key == "Tel":
                self.musTel = value
            elif key == "Oda":
                self.Oda = value
                self.odaBilgi = Dt(adres="odaBilgi",ALANLAR=["Kat","OdaNumara","DoluBos"])
            elif key == "GunSay":
                self.GunSay = value
        self.kayitOlustur()

    def kayitOlustur(self):
        self.MusKayit = Dt(adres="musteri",ALANLAR=["Adı","Soyadı","Tel","Oda","GunSay","Zaman"])
        self.MusKayit.iduComp(self.musAd,self.musSoyad,self.musTel,self.Oda,self.GunSay,self.Bas,param=1)
        self.odaGuncelle()

    def odaGuncelle(self,doluBos = "DOLU"):
        kat = self.Oda[0] + "_KAT"
        id = ((int(self.Oda[0])-1)*5) + int(self.Oda[2])
        oda = self.Oda
        self.odaBilgi.iduComp(kat,oda,doluBos,param=2,ID=id)

deneme = OtelMusteri(Ad="İbrahim",Soyad="Ediz",Tel="05052643514",Oda="204",GunSay="5")
