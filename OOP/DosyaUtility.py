import os
class DosyaTool():
    dosyaUzanti = ".csv"
    def __init__(self,adres="isimyok",**kwargs):
        self.adres = os.getcwd()+os.sep+adres+self.dosyaUzanti
        self.dosya = None
        self.dosyaAc()
        self.sozluk = kwargs
    print(__name__)
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

    def girisAl(self):
        sonuc = ""
        for key,value in self.sozluk.items():
            if key=="ALANLAR":
                for item in value:
                    sonuc+= input(item + " giriniz ") + ";"
        sonuc = sonuc.rstrip(";") + "\n"
        return sonuc
    
    def idu(self,param=0):
        self.Listele()
        kayit = ""
        liste = self.dosyaOku()
        # ekleme
        if param == 1:
            kayit = self.girisAl()
            liste.insert(0,kayit)
        #düzeltme
        elif param == 2:
            kayitID = int(input("Düzenlenecek Kaydı Seç"))
            kayit = self.girisAl()
            liste[kayitID-1] = kayit
        #silme
        elif param==3:
            kayitID = int(input("Silinecek Kaydı Seç"))
            liste.pop(kayitID-1)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(liste)
        self.dosya.close()
if __name__ == "__main__":
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