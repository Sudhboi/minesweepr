import pyautogui as pg

refx, refy = pg.locateCenterOnScreen('resetbutton.png', confidence = 0.5) #1636 420
refx, refy = int(refx), int(refy)
pos0x , pos0y = refx - 121, refy + 34 #1515 454

def return_coordinates(x, y):
    return pos0x + (16 * x), pos0y + (16 * y)

def click_tile(x, y):
    rx, ry = return_coordinates(x, y)
    pg.moveTo(rx, ry, 0.5)
    pg.click()

def reset():
    pg.moveTo(refx, refy)
    pg.doubleClick()
    print(refx, refy)

