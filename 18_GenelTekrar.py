a = 1
b= 1
for i in range(0,21):
    c = a + b
    print(i,"-",c)
    a,b = b,c
else:
    print("Bitti")

liste = [1,2,3,4,5,6]
metin = "tripanazomigambiyetsiz"
for item in metin:
    print(item)
liste = [i for i in range(0,20)]
sozluk = {liste[i]:i*2 for i in range(0,len(liste)) }
print(sozluk)
# anahtar = 1
# while True:
#     i+=1
#     print(i)
#     if input("Çıkış?").upper() == "Ç":
#         break
# else:



