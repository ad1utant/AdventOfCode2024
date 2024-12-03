import re
count = 0

with open('3_data.txt', 'r') as file:
    for line in file:
        tab = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    for item in tab:
        pair = list(map(int, re.findall(r'(\d+)', item)))
        count += pair[0]*pair[1]
print(count)