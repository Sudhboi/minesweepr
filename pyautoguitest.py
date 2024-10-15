import pyautogui as pg

refx, refy = pg.locateCenterOnScreen('resetbutton.png') #1636 420
pos0x , pos0y = refx - 121, refy + 34 #1515 454

def return_coordinates(x, y):
    return pos0x + (16 * x), pos0y + (16 * y)

def click_tile(x, y):
    pg.moveTo(return_coordinates(x, y))
    pg.click()

def reset():
    pg.moveTo(refx, refy)
    pg.click()
    print(refx, refy)


reset()
click_tile(7, 7)
