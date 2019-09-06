import os
class DosyaTool():
    __dosyaUzanti = ".csv"
    __dosyalistesi = []
    def __init__(self,adres="isimyok",**kwargs):
        self.adres = os.getcwd()+os.sep+adres+self.dosyaUzantisi
        self._isim = adres
        self.dosya = None
        self.dosyaAc()
        self.sozluk = kwargs
        self.dosyaListeEkle()
    def dosyaisimguncelle(self):
        dosya = open(self.adres)
        metin =  dosya.read()
        self.adres = os.getcwd()+os.sep+self.isim+self.dosyaUzantisi
        yeniDosya = open(self.adres,"w")
        yeniDosya.write(metin)
        yeniDosya.close()

    def dosyaListeEkle(self):
        self.__dosyalistesi.append(self._isim)

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self,yeni_deger):
        indis = self.__dosyalistesi.index(self._isim)
        self.__dosyalistesi[indis] = yeni_deger
        self._isim = yeni_deger
        self.dosyaisimguncelle()

        

    @property
    def dosyaUzantisi(self):
        return self.__dosyaUzanti

    @dosyaUzantisi.setter
    def dosyaUzantisi(self,yenideger):
        if yenideger.startswith(".") and yenideger in [".txt",".csv"]:
            self.__dosyaUzanti = yenideger
            return self.__dosyaUzanti
        else:
            return None

    @dosyaUzantisi.deleter
    def dosyaUzantisi(self):
        del self.__dosyaUzanti

    @classmethod
    def dosyaListesiYazdir(cls):
        print("Dosya Listesi")
        for item in cls.__dosyalistesi:
            print(item)
    

    @staticmethod
    def piNumber():
        print(22/7)

    def dosyaAc(self):
        if os.path.exists(self.adres):
            dosya = open(self.adres,"r+")
        else:
            dosya = open(self.adres,"w+")
        self.dosya = dosya

    def arama(self,param=""):
        liste = self.dosyaOku()
        sonucListesi = []
        for item in liste:
            for i in item.split(";"):
                if  param.upper() in i.upper():
                    sonucListesi.append(item)
        return sonucListesi

    
    def AramaCagir(self):
        aramaKelime = input("aramak istediğinizi yazınız")
        sonuc = self.arama(aramaKelime)
        self.EkranaListeYaz(sonuc)
        

    def dosyaOku(self):
        self.dosyaAc()
        self.dosya.seek(0)
        liste = self.dosya.readlines()
        return liste

    def EkranaListeYaz(self,liste=[]):
        metin = ""
        for i in range(0,len(liste)):
            metin = "{}".format((i+1))
            for item in liste[i].split(";"):
                metin += "-" +item 
            print(metin)
        self.dosya.close()

    def Listele(self):
        liste = self.dosyaOku()
        self.EkranaListeYaz(liste)
       

    def girisAlUser(self):
        sonuc = ""
        for key,value in self.sozluk.items():
            if key=="ALANLAR":
                for item in value:
                    sonuc+= input(item + " giriniz ") + ";"
        sonuc = sonuc.rstrip(";") + "\n"
        return sonuc
    
    def girisAlComp(self,):
        sonuc = ""
        for key,value in self.sozluk.items():
            if key=="ALANLAR":
                for i in range(0,len(value)):
                # for item in value:
                    sonuc+= self.girisler[i] + ";"
        sonuc = sonuc.rstrip(";") + "\n"
        return sonuc
    
    def iduUser(self,param=0):
        self.Listele()
        kayit = ""
        liste = self.dosyaOku()
        # ekleme
        if param == 1:
            kayit = self.girisAlUser()
            liste.insert(0,kayit)
        #düzeltme
        elif param == 2:
            kayitID = int(input("Düzenlenecek Kaydı Seç"))
            kayit = self.girisAlUser()
            liste[kayitID-1] = kayit
        #silme
        elif param==3:
            kayitID = int(input("Silinecek Kaydı Seç"))
            liste.pop(kayitID-1)
        self.kaydet(liste)


    def iduComp(self,*args,param=0,ID = 0):
        self.girisler = args
        kayit = ""
        liste = self.dosyaOku()
        # ekleme
        if param == 1:
            kayit = self.girisAlComp()
            liste.insert(0,kayit)
        #düzeltme
        elif param == 2:
            kayitID = ID
            kayit = self.girisAlComp()
            liste[kayitID-1] = kayit
        #silme
        elif param==3:
            kayitID = ID
            liste.pop(kayitID-1)
        self.kaydet(liste)

    def kaydet(self,liste=[]):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(liste)
        self.dosya.close()


    def temizle(self):
        self.dosyaAc()
        self.kaydet()
if __name__ == "__main__":
    dt = DosyaTool(ALANLAR=["bos","bos1"])
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
            dt.iduUser(islem)
        elif islem == 4:
            dt.Listele()
        elif islem == 5:
            dt.AramaCagir()
        elif islem == 6:
            anahtar = 0
        else:
            print("Menü Dışında Seçenek Girdin ")
    else:
        print("İyi Günler Dileriz")
