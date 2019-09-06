# import tkinter as tk
# import time
# pencere = tk.Tk()

# def cikis():
#     etiket["text"] = "Görüşmek Üzere"
#     dugme["text"] = "Bekleyiniz"
#     dugme["state"] = "disable"
#     pencere.after(2000,pencere.destroy)

# pencere.geometry('200x300')
# etiket = tk.Label(text="Merhaba Vektorel Python")
# etiket.pack()

# dugme = tk.Button(text="Çıkış",command=cikis)
# dugme.pack()

# pencere.protocol("WM_DELETE_WINDOW",cikis)


# pencere.mainloop()


import tkinter as tk

class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW",self.cikis)
        self.etiket = tk.Label(text="Merhaba Vektorel Python")
        self.etiket.pack()

        self.dugme = tk.Button(text="Çıkış",command=self.cikis)
        self.dugme.pack()
    
    def cikis(self):
        self.etiket["text"] = "Görüşmek Üzere"
        self.dugme["text"] = "Bekleyiniz"
        self.dugme["state"] = "disable"
        self.after(2000,self.destroy)

pencere = Pencere()
pencere.mainloop()
