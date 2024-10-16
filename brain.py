# Handles Processing

def get_surround(x, y, state_array):
    # [topleft, top, topright, left, right, botleft, bot, botright]

    points = [state_array[y - 1][x - 1] if x > 0 and y > 0 else 'N',
              state_array[y - 1][x] if y > 0 else 'N',
              state_array[y - 1][x + 1] if x < 15 and y > 0 else 'N',
              state_array[y][x - 1] if x > 0 else 'N',
              state_array[y][x + 1] if x < 15 else 'N',
              state_array[y + 1][x - 1] if x > 0 and y < 15 else 'N',
              state_array[y + 1][x] if y < 15 else 'N',
              state_array[y + 1][x + 1] if x < 15 and y < 15 else 'N']
    
    return points

def get_points(state_array, flag):
    points = []
    for row in range(16):
        for elem in range(16):
            if state_array[row][elem] in ['1', '2', '3', '4', '5', '6', '7', '8']:
                surr_elems = get_surround(elem, row, state_array)
                print(elem, row, state_array[row][elem], surr_elems)
                if (surr_elems.count('C') + surr_elems.count('F') if flag else surr_elems.count('F')) == int(state_array[row][elem]):
                    for i in range(8):
                        if surr_elems[i] == 'C':
                            if i == 0 and (elem - 1, row - 1) not in points: points.append((elem - 1, row - 1))
                            if i == 1 and (elem, row - 1) not in points: points.append((elem, row - 1))
                            if i == 2 and (elem + 1, row - 1) not in points: points.append((elem + 1, row - 1))
                            if i == 3 and (elem - 1, row) not in points: points.append((elem - 1, row))
                            if i == 4 and (elem + 1, row) not in points: points.append((elem + 1, row))
                            if i == 5 and (elem - 1, row + 1) not in points: points.append((elem - 1, row + 1))
                            if i == 6 and (elem, row + 1) not in points: points.append((elem, row + 1))
                            if i == 7 and (elem + 1, row + 1) not in points: points.append((elem + 1, row + 1))
    return points

def clean_up(state_array):
    for row in range(16):
        for elem in range(16):
            if state_array[row][elem] == 'C':
                return [(elem, row)]
    return []
            
def recognize_game_over(state_array):
    tiles = []
    [tiles.extend(i) for i in state_array]
    print(tiles)
    if tiles.count("T") != 0:
        return "Mine Triggered"
    elif tiles.count("M") == 40:
        return "Won!"
    else:
        return False


