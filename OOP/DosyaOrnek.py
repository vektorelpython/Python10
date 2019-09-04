from OOP.DosyaUtility import DosyaTool as Dt

# teldefter = DosyaTool(adres="teldefter",ALANLAR=["Adı","Soyadı","Telefon"])
# teldefter.iduComp("Oğuzhan","Python","101",param=2,ID=1)
# teldefter.Listele()



odaOtelBilgi = Dt(adres="odaBilgi",ALANLAR=["Kat","OdaNumara","DoluBos"])
# odaOtelBilgi.temizle()
# for i in range(3,0,-1):
#     for j in range(1,6):
#         odaOtelBilgi.iduComp(str(i)+"_KAT",str(i)+"0"+str(j),"Boş",param=1)



print(Dt.dosyaUzantisi)
deneme = Dt(adres="deneme",ALANLAR=["1","2"])

