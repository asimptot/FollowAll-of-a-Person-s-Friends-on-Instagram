import pyautogui as pg
import time
from tkinter import *

def butonKomutlari():
    follower = giris1.get()
    URL = "www.instagram.com/"+giris2.get()

    sayi =0
    sayi=int(follower)

    pg.press('win')
    pg.typewrite('chrome.exe')
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.typewrite(URL)
    pg.press('enter')
    time.sleep(2)

    ##

    for m in range(6):
        pg.press('tab')
        time.sleep(0.5)
    pg.press('enter')
    time.sleep(5)

##
    for j in range(0, sayi*4, 4):
        if j == 32:
            for m in range(71):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(5)
        else:
            for k in range(5+j):
                pg.press('tab')
                time.sleep(0.25)
            pg.press('enter')
            time.sleep(5)


p = Tk()
p.title("Takip İşlemi Yapan Sistem")
p.geometry("750x500+500+200")

bilgilendirme = Label(p, text="Chrome'da Login Bilgilerinizin Tutulduğuna Emin Olunuz")
bilgilendirme.grid(row=0, column=0, columnspan=2)

bilgilendirme1 = Label(p, text="Takip Edilecek Takipçi Adedi Girin")
bilgilendirme1.grid(row=1, column=2, columnspan=1)
s1Lbl = Label(p, text="Takip Adedi: ")
s1Lbl.grid(row=1, column=0)

s2Lbl = Label(p, text="Instagram Kullanıcı Adı: ")
s2Lbl.grid(row=2, column=0)

giris1 = Entry(p)
giris1.grid(row=1, column=1)

giris2 = Entry(p)
giris2.grid(row=2, column=1)

dugme = Button(p, text="Başlat", command=butonKomutlari)
dugme.grid(row=12, column=1, sticky=E)

p.mainloop()