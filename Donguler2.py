# import random
# sayi =  random.randint(1,50)
# buyukliste = []
# kolonSay = int(input("Kolon Sayısı Giriniz"))
# for j in range(0,kolonSay):
#     liste = []
#     for i in range(0,6):
#         sayi =  random.randint(1,50)
#         while sayi in liste:
#             sayi =  random.randint(1,50)
#         liste.append(sayi)
#     liste.sort()
#     buyukliste.append(liste)
# print(*buyukliste,sep="\n")

# for item in buyukliste:
#     print(item)

#Faktoriyel Sorusu
sayi = int(input("Sayıyı Giriniz"))
sonuc = 1
for i in range(1,sayi+1):
    sonuc *=i
print(sonuc)

"""
Ekran görülen kod sayısal loto oynar
kaç defa oynamak istediğini kullanıcıdan alıp 
o kadar sonuç üretecek şekilde kodunuzu genişletin


Girilen Sayının Faktöriyelini ekrana yazan programı yazınız
"""  

"""
Çalışma Sorusu
Kullanıcı tarafından girilen tutarın yazı ile ekrana yazılmasını sağlayan
programı yazınız
örnek : Girdi: 9,845,741,852
örnek : Çıktı: Dokuz Milyar Sekiz Yüz Kır Beş Milyon Yedi Yüz Kırk Bir
Bin Sekiz Yüz Elli İki
"""