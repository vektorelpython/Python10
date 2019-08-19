# def fonk(*args,a=1):
#     sonuc = 0
#     for item in args:
#         sonuc += item
#     return sonuc

# print(fonk(1,2,3,4,6,7,8,9,a=2))

def fonk2(**kwargs):
    for key,value in kwargs.items():
        print("Parametre Adı:",key)
        print("Değer:",value)
fonk2(TABLO="ST_ILLER",SUTUN=["IL_ADI","IL_KODU"])


# fonk3 = lambda x,y: x*y
# print(fonk3(3,5))


def outerFunction(a):
        a = 5
        def innerfunction(a):
                a = 8
                return a
        innerfunction(a)
        return a

print(outerFunction(2))