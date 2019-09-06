from OOP.DosyaUtility import DosyaTool

kayit1 = DosyaTool("teldefter",ALANLAR=["1","2"])
kayit2 = DosyaTool("kayit2",ALANLAR=["1","2"])
DosyaTool.dosyaListesiYazdir()
kayit1.isim = "yeni"

DosyaTool.dosyaListesiYazdir()