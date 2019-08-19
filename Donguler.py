a=1
b=1
# for i in range(1,11):
#     c = a+b
#     print("Serinin {}. Terimi:{}".format(i,c))
#     a,b = b,c
# for i in range(10,1,-1):
#     print(i)
# for i in range(0,100,5):
#     print(i)

import time
liste = ["Yalan","söyleme","gözlerime","bak"]
for item in liste:
    time.sleep(1)
    print(item)
for i in range(1,len(liste)+1):
    time.sleep(5%i)
    print(liste[i-1])

metin = "BEŞİKTAŞ"
for i in metin:
    print(i)

