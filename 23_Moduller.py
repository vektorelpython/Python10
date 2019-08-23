import sys
# if sys.version_info.major == 3:
#     print(sys.version_info.major)

# print(sys.getwindowsversion())
# print(*sys.path,sep="\n")

# sys.path.append("D:\EDZDatabase")
# print(*sys.path,sep="\n")


import random
print(random.random())
print(random.uniform(0.0,0.5))
print(random.randint(0,100))

liste = ["ali","veli","ışıl","cesim","mahmut"]
print(random.choice(liste))


l = list(range(10))
print(liste)
random.shuffle(liste)
print(liste)
print(random.randrange(100))

liste = list(range(1,50))
sonuc = random.sample(liste,6)
sonuc.sort()
print(sonuc)

