#Performs actions and delegates tasks

import actionmanager 
import imageprocessor 
import brain

state_image = actionmanager.screenshot_board_state()
state_array = imageprocessor.convert_to_array(state_image)
points = brain.get_point_flag(state_array)
print(points)
actionmanager.execute_actions(points, True)


# state = 0 # 0 - Flagging, 1 - Checking, 2 - Guessing
# isRunning = True

# while isRunning:
#     if state == 0:
#         points = brain.get_points_for_flag()

