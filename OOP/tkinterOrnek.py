import tkinter as tk
import time
pencere = tk.Tk()

def cikis():
    etiket["text"] = "Görüşmek Üzere"
    dugme["text"] = "Bekleyiniz"
    dugme["state"] = "disable"
    pencere.after(2000,pencere.destroy)

pencere.geometry('200x300')
etiket = tk.Label(text="Merhaba Vektorel Python")
etiket.pack()

dugme = tk.Button(text="Çıkış",command=cikis)
dugme.pack()

pencere.protocol("WM_DELETE_WINDOW",cikis)


pencere.mainloop()
