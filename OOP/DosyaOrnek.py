from OOP.DosyaUtility import DosyaTool as Dt
from datetime import datetime as dt
class OtelMusteri():
    __otelisim = "Turist"
    def __init__(self,*args,**kwargs):
        self.musSoyad = ""
        self.musTel = ""
        self.Oda = ""
        self.GunSay = ""
        self.Bas = dt.date()
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


    def odaGuncelle