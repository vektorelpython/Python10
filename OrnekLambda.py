liste = ["ışınsu","çiğdem","ışıl","yeter","imdat"]
alfabe = "abcçdefghıijklmnoöprsştuüvyz"
cevrim = {i: alfabe.index(i) for i in alfabe}
print(cevrim)
print(sorted(liste,key=lambda x: cevrim.get(x[0])))
