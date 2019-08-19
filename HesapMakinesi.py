islemMenu = """
1-Topla
2-Çıkar
3-Böl
4-Çarp
"""
print(islemMenu)
islem = input("islem numarasını giriniz")
if islem:
    sayi1 = int(input("1. Sayıyı giriniz"))
    sayi2 = int(input("2. Sayıyı giriniz"))
    if islem == "1":
        sonuc = "{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2)
    elif islem == "2":
        sonuc = "{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2)
    elif islem == "3":
        sonuc = "{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2)
    elif islem == "4":
        sonuc = "{} * {} = {}".format(sayi1,sayi2,sayi1*sayi2)
    print(sonuc)
else:
    print("Giriş Yapmadınız")
