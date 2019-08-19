#adi = input("Adınızı Giriniz")
#print("Merhaba",adi)
#sep
#end
#file
"""
merhaba
nasılsın
"""
##print("KAT","LANA","RAK",sep="\n",end="")
dosya = open("deneme.csv","a+")
adi = input("Adınızı Giriniz")
soyadi = input("Soyadınızı Giriniz")
telefon = input("Telefon Numarası Giriniz")
print(adi,soyadi,telefon,sep=";",end="\n",file=dosya)

import keyword
print(*keyword.kwlist,sep="\n")
"deneme".
