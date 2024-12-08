tab = []
position = None
with open('6_data.txt','r') as file:
    line_index, char_index = 0, 0
    for line in file:
        line = line.strip('\n')
        tab.append([])
        for char in line:
            if char == '^':
                position = [line_index, char_index]
            tab[-1].append(char)
            char_index += 1
        char_index = 0
        line_index += 1

start_position = position[:]
count = 0
param = 'U'
run  = True
tab[position[0]][position[1]] = 'X'
x_list, list_of_params_and_positions = [],[]

def check_move(position, optional_param, param, tab, x_value, y_value, *args):
    y, x = position[0], position[1]
    try:
        if tab[y + y_value][x + x_value] == '#':
            return True, tab, position, optional_param, list_of_params_and_positions
        else:
            position = [y + y_value, x + x_value]
            tab[position[0]][position[1]] = 'X'
            global start_position
            if [position, param] in list_of_params_and_positions and not [position, param] == [start_position, 'U']:
                global count
                count += 1
                return False, tab, position, optional_param, list_of_params_and_positions

            list_of_params_and_positions.append([position, param])
            x_list.append(position)
            return True, tab, position, param, list_of_params_and_positions
    except IndexError:
        return False, tab, position, param, list_of_params_and_positions

def set_param(param):
    match param:
        case 'U':
            return 0, -1, 'R'
        case 'D':
            return 0, 1, 'L'
        case 'R':
            return 1, 0, 'D'
        case 'L':
            return -1, 0, 'U'

while run:
    x_value, y_value, optional_param = set_param(param)
    run, tab, position, param, list_of_params_and_positions = check_move(position, optional_param, param, tab, x_value, y_value)
positions_to_check = x_list[:]

for item in positions_to_check:
    tab[item[0]][item[1]] = '#'
    position = start_position
    list_of_params_and_positions = []
    param = 'U'
    run = True


    while run:

        x_value, y_value, optional_param = set_param(param)
        run, tab, position, param, list_of_params_and_positions = check_move(position, optional_param, param, tab, x_value, y_value, list_of_params_and_positions)


    tab[item[0]][item[1]] = 'X'
    print(f'{count}/{len(positions_to_check)}')
print(count)
