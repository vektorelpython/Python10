# var1 = "      Ali;Veli;Deli         "
# var2 = 2
# var3 = 1.2
# var4 = 1.2j
# var5 = [1,2,3]
# var6 = (1,2,"a")
# var7 = {"1":"Bir"}
# var8 = False

# var1 = "www.vektorelbilisim.com"
# # var1 = var1.replace(".com","").replace("www.","")
# print(var1.split(".")[1])
# var1 = "merhaba"
# print(var1)
# var1 = [1,2,2,3,[23,1],"aaa"]

# var1.append("bbb")
# var1.insert(1,["a","b","c"])
# print(var1)
# var1.remove("aaa")
# print(var1)
# print(var1.pop(0))
# print(var1)

# var2 = [1,2,3,4,5,6,7,8,9,10]
# print(var2)
# print(var2[8:1:-2])
# var2 = var1
# a = 2
# b = 3
# a = b
# a = 5


# var1 = [1,2,3,4,5,1,1,1,1]
# var2 = var1
# var3 = var1.copy() 
# var2[2] = 10
# var3[4] = 20
# print(var1)
# print(var2)
# print(var3)
# var1.reverse()
# print(var1)
# var1.sort()
# print(var1)

# metin1 = "ALi"
# metin2 = metin1
# metin2 = "VELİ"
# print(metin1)
# print(metin2)


# demet = (1,)

# sozluk = {"kitap":"book",}
# sozluk["kitap"] ="Buch"
# print(sozluk["kitap"])
# sozluk.update({"pencil":"Kalem"})
# print(sozluk)
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())
# print(sozluk.get("demet"))

# liste = ["1","2","3","4"]
# sozluk = dict.fromkeys(liste,"0")
# print(sozluk)
# # print(sozluk.pop(1))
# sozluk.popitem()
# print(sozluk)
# sozluk.popitem()
# print(sozluk)
# a = int(input("Parametre Giriniz"))
# if a == 2 and not a < 0:
#     print("parametre 2 geldi")
# elif a == 1:
#     print("parametre 1 geldi")
# elif a == 3:
#     print("parametre 3 geldi")
# else:
#     print("parametre",a)

# var2 is not var1
# metin = "BEŞİKTAŞ"
# "B" not in metin
# 2 AND ve
# 3 OR veya
# 1 NOT

# liste = [i for i in range(1,20)]
# sozluk = {liste[i]:i*2 for i in range(0,len(liste)) }
# print(sozluk)

metin =  input("Giriş Yapınız")
if metin:
    print("Giriş Başarılı")
else:
    print("Giriş Yapmadınız")
