import pyautogui as pg
import time

def open_wo_login():
    pg.click(333, 752)
    time.sleep(2)

def refresh():
    pg.click(86, 49)  # refresh
    time.sleep(8)

def follower_list():
    for m in range(6):
        pg.press('tab')
        time.sleep(2)
    pg.press('enter')
    time.sleep(5)

def follow_all():
    for j in range(0, 100, 4):
        for k in range(5+j):
            pg.press('tab')
            time.sleep(2)
        pg.press('enter')
        time.sleep(5)

def main():
    open_wo_login()
    refresh()
    follower_list() #takipçi listesi
    follow_all()

    pg.click(860, 238) #close
    time.sleep(3)

main()



