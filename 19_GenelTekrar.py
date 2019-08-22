# def Fonk(a = 1,b = 1):
#     return a
# Fonk(1,2)
# Fonk(b=1,a=2)

# def Fonk2(*args,b=1):
#     sonuc = 0
#     for item in args:
#         sonuc += item
#         # print(args)
#     return sonuc
# print(Fonk2(1,2,3,4,5,6,7,b=5))

# def Fonk3(**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         if key == "PARAM1":
#             print("Montumun cebinde yok kuruş")
#         elif key == "PARAM2":
            
#             print(value,"Günah benim suç benim")

# Fonk3(PARAM1=[1,2,3,4],PARAM2="aaaaa")


def Fonk2(*args,b=1):
    sonuc = 0
    for item in args:
        sonuc += item
        # print(args)
    return sonuc,args

print(Fonk2(1,2,3,4,5))
print(Fonk2(1,2,3,4,5)[0])
print(Fonk2(1,2,3,4,5)[1])


