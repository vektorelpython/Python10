
"""
Kullanıcı tarafından girilen tutarın yazı ile ekrana yazılmasını sağlayan
programı yazınız
örnek : Girdi: 9,845,845,802
örnek : Çıktı: Dokuz Milyar Sekiz Yüz Kır Beş Milyon Yedi Yüz Kırk Bir
Bin Sekiz Yüz Elli İki
"""
456852741852963
# metin = input("Tutarı Giriniz")
basamak =  {
0:"",
1:" Bin ",
2: " Milyon ",
3:" Milyar ",
4:"Trilyon"
}

birler = {
    "0":"",
    "1":" Bir",
    "2":" İki",
    "3":" Üç ",
    "4":" Dört",
    "5":" Beş",
    "6":" Altı",
    "7":" Yedi",
    "8":" Sekiz",
    "9":" Dokuz"}
onlar = {
    "0":"",
    "1":" On ",
    "2":" Yirmi ",
    "3":" Otuz ",
    "4":" Kırk ",
    "5":" Elli ",
    "6":" Altmış ",
    "7":" Yetmiş ",
    "8":" Seksen ",
    "9":" Doksan "
}
metin = input("Tutarı Giriniz")
metin = metin.replace(",","").replace(".","")
while len(metin)%3 > 0:
    metin = "0" + metin
liste = []

for i in range(0,int(len(metin)/3)):
    liste.append(metin[i*3:(i*3)+3])

sonuc = ""
for i in range(0,len(liste)):
    item = liste[i]
    if item[0] != "0":
        if item[0] != "1":
            sonuc += birler[item[0]] + " yüz "
        else:
            sonuc += " yüz "
    sonuc += onlar[item[1]]
    sonuc += birler[item[2]]
    sonuc += basamak[(len(liste)-1)-i]
print(sonuc)
input()