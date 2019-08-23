import os
print(os.getcwd())
print(os.sep)
# dosya = open("deneme.csv","r+")
# for i in os.listdir(os.curdir):
#     print(i)
# print(os.listdir('.'))
# print(os.pardir)
# os.chdir
# os.mkdir
# demet = os.stat("teldefter.csv")
# print(demet)
# for i in demet:
#     print(i)
# os.system(r"C:\Users\vektorel\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
# C:\ProgramData\Anaconda3\pythonw.exe 
# C:\ProgramData\Anaconda3\cwp.py 
# C:\ProgramData\Anaconda3 
# C:\ProgramData\Anaconda3\pythonw.exe 
# C:\ProgramData\Anaconda3\Scripts\anaconda-navigator-script.py


import os
def tara(dizin):
    basla = os.getcwd()
    dosyalar = []
    os.chdir(dizin)

    for item in os.listdir(os.curdir):
        if not os.path.isdir(item):
            dosyalar.append(item)
        else:
            try:
                dosyalar.extend(tara(item))
            except:
                pass
    os.chdir(basla)
    return dosyalar


# for kokdizin,dizinler,dosyalar in  os.walk(r"D:\İbrahim EDİZ"):
#     print(kokdizin,dizinler,dosyalar,sep="\n")
metin = "Nilay İrem Göktürk;Fatih Sarıkaya;Mustafa KESER;Oğuzhan Çakır;Lütfullah Yasin Güzel;Kutlu Mızrak;Burak Berk BAŞKAYA"
for item in metin.split(";"):
    adres = os.path.join(os.getcwd(),item)
    os.mkdir(adres)
