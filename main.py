#Performs actions and delegates tasks

import random
import actionmanager 
import imageprocessor 
import brain

def start():
    actionmanager.reset()
    closed = []
    while closed.count("O") == 0 and closed.count("M") == 0:
        actionmanager.click_tile(random.randint(0, 15), random.randint(0, 15))
        state_image = actionmanager.screenshot_board_state()
        state_array = imageprocessor.convert_to_array(state_image)
        [closed.extend(i) for i in state_array]

start()
points = ['a']
while points != []:
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


# state = 0 # 0 - Flagging, 1 - Checking, 2 - Guessing
# isRunning = True

# while isRunning:
#     if state == 0:
#         points = brain.get_points_for_flag()

