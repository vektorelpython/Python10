sayi = int(input("Sayıyı Giriniz"))
sonuc = 0
for i in range(1,sayi):
    if sayi%i == 0:
        sonuc += i
    else:
        continue
    if sonuc == sayi:
        print("Mükkemmel")

