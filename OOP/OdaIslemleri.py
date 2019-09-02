from DosyaUtility import DosyaTool as DB


class OdaJob():
    def __init__(self,*args,**kwargs):
        self.OdaDB = DB(adres="odaBilgisi",ALANLAR=["Kat","OdaNum","Dolu"])
        
    def odaEkle(self):
        self.OdaDB.idu(param=1,param2=1,Kat="1",OdaNum="102",Dolu="1")


deneme = OdaJob()
deneme.odaEkle()