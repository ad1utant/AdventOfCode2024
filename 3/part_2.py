import re
count = 0
flag = True
correct_string = ''

with open('3_data.txt', 'r') as file:
    for line in file:
        for i in range(len(line)):
            try:
                if line[i] == 'd' and line[i+1] == 'o' and line[i+2] == '(' and line[i+3] == ')':
                    flag = True
                if line[i] == 'd' and line[i+1] == 'o' and line[i+2] == 'n' and line[i+3] == "'" and line[i+4] == 't' and line[i+5] == '(' and line[i+6] == ')':
                    flag = False
            except IndexError:
                break
            if flag:
                correct_string += line[i]

tab = re.findall(r'mul\(\d{1,3},\d{1,3}\)', correct_string)
for item in tab:
    pair = list(map(int, re.findall(r'(\d+)', item)))
    count += pair[0]*pair[1]
print(count)