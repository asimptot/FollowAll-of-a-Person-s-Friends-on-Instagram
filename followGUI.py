import pyautogui as pg
import time
from tkinter import *
import subprocess

def follow_list():
    time.sleep(10)

    for m in range(6):
        pg.press('tab')
        time.sleep(1)
    pg.press('enter')
    time.sleep(5)

def close():
    for m in range(1):
        pg.hotkey('alt', 'f4')

def open_browser():
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(2)

def follow_all(sayi, sayac):

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

            sayac=sayac+1
            etiket = Label(p, fg="green")
            etiket.grid(row=3, column=0)
            etiket.config(text=str(sayac))
    return sayi

def butonKomutlari():
    time.sleep(3)
    Liste =[giris2, giriss2, girisss2]
    follower = giris1.get()

    for i in range(3):
        URL = "www.instagram.com/" + Liste[i].get()
        sayac = 0
        sayi=int(follower)

        open_browser()
        pg.typewrite(URL)
        pg.press('enter')
        time.sleep(2)

        follow_list()
        follow_all(sayi, sayac)

    for i in range(3):
        close()

p = Tk()
#p.wm_iconbitmap('follow.ico')
#p.wm_title('Title')
p.title("Follows the Followers of an Instagram Account 4.1")
p.geometry("800x200")

bilgilendirme = Label(p, text="*Make Sure Your Instagram Account is Login in Chrome*")
bilgilendirme.grid(row=0, column=0, columnspan=2)

s1Lbl = Label(p, text="Follow Count")
s1Lbl.grid(row=1, column=0)

s2Lbl = Label(p, text="www.instagram.com/")
s2Lbl.grid(row=2, column=0)

s3Lbl = Label(p, text="www.instagram.com/")
s3Lbl.grid(row=3, column=0)

s4Lbl = Label(p, text="www.instagram.com/")
s4Lbl.grid(row=4, column=0)

bilgilendirme2 = Label(p, text="Instagram Nickname")
bilgilendirme2.grid(row=2, column=2, columnspan=1)

bilgilendirme3 = Label(p, text="Instagram Nickname")
bilgilendirme3.grid(row=3, column=2, columnspan=1)

bilgilendirme4 = Label(p, text="Instagram Nickname")
bilgilendirme4.grid(row=4, column=2, columnspan=1)

giris1 = Entry(p, width="10")
giris1.grid(row=1, column=1)

giris2 = Entry(p, width="10")
giris2.grid(row=2, column=1)

giriss2 = Entry(p, width="10")
giriss2.grid(row=3, column=1)

girisss2 = Entry(p, width="10")
girisss2.grid(row=4, column=1)

dugme = Button(p, text="Follow", command=butonKomutlari)
dugme.grid(row=12, column=1, sticky=E)

p.mainloop()
