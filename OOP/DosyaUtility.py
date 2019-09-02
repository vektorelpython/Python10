import os
class DosyaTool():
    dosyaUzanti = ".csv"
    def __init__(self,adres="isimyok",**kwargs):
        self.adres = os.getcwd()+os.sep+adres+self.dosyaUzanti
        self.dosya = None
        self.dosyaAc()

    def dosyaAc(self):
        if os.path.exists(self.adres):
            dosya = open(self.adres,"r+")
        else:
            dosya = open(self.adres,"w+")
        self.dosya = dosya

    def dosyaOku(self):
        self.dosyaAc()
        self.dosya.seek(0)
        liste = self.dosya.readlines()
        return liste

    def Listele(self):
        liste = self.dosyaOku()
        metin = ""
        for i in range(0,len(liste)):
            metin = "{}".format((i+1))
            for item in liste[i].split(";"):
                metin += "-" +item 
            print(metin)
        self.dosya.close()
        