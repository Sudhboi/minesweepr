#Handles Actions

import pyautogui as pg

pg.MINIMUM_DURATION = 0.1
pg.MINIMUM_SLEEP = 0
pg.PAUSE = 0

refx, refy = pg.locateCenterOnScreen('resources\\resetbutton.png', confidence = 0.5) 
refx, refy = int(refx), int(refy)
print("Reference Button Located Successfully.")
pos0x , pos0y = refx - 121, refy + 34 

def return_coordinates(x, y):
    return pos0x + (16 * x), pos0y + (16 * y)

def click_tile(x, y, flag = False):
    rx, ry = return_coordinates(x, y)
    pg.moveTo(rx, ry)
    if flag == False:
        pg.click()
    if flag == True:
        pg.rightClick()
    print("Clicked {}, {} at {}, {}.".format(x, y, rx, ry))

def reset():
    pg.moveTo(refx, refy)
    pg.doubleClick()
    print("Reset Successful.")

def screenshot_board_state(): #Not as efficient as reading only the necessary squares, but more thorough
    pg.moveTo(refx - 30, refy)
    reg = (pos0x - 7, pos0y - 7, 256, 256)
    state = pg.screenshot(region=reg)
    print("Board State Returned Successfully")
    return state  

def screenshot_tile(x, y, name): #Temporary, used for development
    sx, sy = return_coordinates(x, y)
    reg = (sx - 7, sy - 7, 16, 16)
    screenshot = pg.screenshot(region=reg)
    screenshot.save("resources\\{}.png".format(name))

def execute_actions(points, flag = False):
    for point in points:
        x, y = point
        click_tile(x, y, flag)


screenshot_tile(10, 7, '6')