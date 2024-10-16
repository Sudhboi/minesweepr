#Handles Actions

import pyautogui as pg

refx, refy = pg.locateCenterOnScreen('resources\\resetbutton.png', confidence = 0.5) 
refx, refy = int(refx), int(refy)
print("Reference Button Located Successfully.")
pos0x , pos0y = refx - 121, refy + 34 

def return_coordinates(x, y):
    return pos0x + (16 * x), pos0y + (16 * y)

def click_tile(x, y):
    rx, ry = return_coordinates(x, y)
    pg.moveTo(rx, ry, 0.5)
    pg.click()
    print("Clicked {}, {} at {}, {}.".format(x, y, rx, ry))

def reset():
    pg.moveTo(refx, refy)
    pg.doubleClick()
    print("Reset Successful.")
