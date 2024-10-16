#Performs actions and delegates tasks

import actionmanager 
import imageprocessor 

state = actionmanager.screenshot_board_state()
state_array = imageprocessor.convert_to_array(state)
for i in state_array:
    print(i)