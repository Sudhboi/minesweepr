#Performs actions and delegates tasks

import random
import actionmanager 
import imageprocessor 
import brain



def start():
    actionmanager.reset()
    closed = []
    while closed.count("O") == 0:
        actionmanager.click_tile(random.randint(0, 15), random.randint(0, 15))
        state_image = actionmanager.screenshot_board_state()
        state_array = imageprocessor.convert_to_array(state_image)
        [closed.extend(i) for i in state_array]
        
        if closed.count("M") > 0:
            return False
    return True

def solve():
    isRunning = True

    if start() == False:
        return "Unlucky Start"
    points = ['a']
    while isRunning:
        state_image = actionmanager.screenshot_board_state()
        state_array = imageprocessor.convert_to_array(state_image)
        points = brain.get_points(state_array, flag = True)
        print(points)
        actionmanager.execute_actions(points, flag = True)

        state_image = actionmanager.screenshot_board_state()
        state_array = imageprocessor.convert_to_array(state_image)
        points = brain.get_points(state_array, flag = False)
        print(points)
        actionmanager.execute_actions(points, flag = False)

        if brain.recognize_game_over(state_array) == "Mine Triggered":
            return "Triggered Mine"

        if brain.recognize_game_over(state_array) == "Won!":
            return "Won"
        
        if points == []:
            cpoints = brain.clean_up(state_array)
            if cpoints == []:
                return "Won"
            actionmanager.execute_actions(cpoints, flag = False)
