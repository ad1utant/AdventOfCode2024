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

count = 0
param = 'U'
run  = True
tab[position[0]][position[1]] = 'X'

def check_move(position, optional_param, param, tab, x_value, y_value):
    y, x = position[0], position[1]
    try:
        if tab[y + y_value][x + x_value] == '#':
            return True, tab, position, optional_param
        else:
            position = [y + y_value, x + x_value]
            tab[position[0]][position[1]] = 'X'
            return True, tab, position, param
    except IndexError:
        return False, tab, position, param
while run:
    match param:
        case 'U':
            x_value, y_value = 0, -1
            optional_param = 'R'
        case 'D':
            x_value, y_value = 0, 1
            optional_param = 'L'
        case 'R':
            x_value, y_value = 1, 0
            optional_param = 'D'
        case 'L':
            x_value, y_value = -1, 0
            optional_param = 'U'
    run, tab, position, param = check_move(position, optional_param, param, tab, x_value, y_value)

for line in tab:
    count += ''.join(line).strip(' ').count('X')
print(count)