import random
devam = "E"
while True:
    if devam.upper() == "E":
        sayi = random.randint(1,100)
        print("Yeni Oyun")
        for i in range(0,5):
            tahmin = int(input("Tahmin Giriniz"))
            if sayi == tahmin:
                print("Tebrikler")
                break
            elif sayi < tahmin:
                print("Aşağı")
            elif sayi > tahmin:
                print("Yukarı")
        else:
            print(sayi)
            print("Game Over")
            devam = input("Devam Etmek İstiyor Musunuz E/H")
    else:
        break
