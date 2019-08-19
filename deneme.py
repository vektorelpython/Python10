dosya = open(r"D:\İbrahim EDİZ\Ornekler\Python Temelleri\aaaa.csv")
liste =  dosya.readlines()
son = []
for item in liste:
    son.append(item.split(";")[1:])

for item in son:
    item[5] = item[5].replace("\n","")

for item in son:
    for i in item:
        i = int(i)




import pandas as pd
df =  pd.DataFrame(son)
print(df.describe())