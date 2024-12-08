from itertools import product, count

characters = ['+', '*']
tab = []
count = 0
with open('7_data.txt', 'r') as file:
    for line in file:
        colon_index = line.index(':')
        tab.append([line[:colon_index], line[colon_index + 2:].strip('\n')])

for pair in tab:
    digits = list(map(int, pair[1].split()))
    count_spaces = len(digits) - 1
    combinations = [''.join(comb) for comb in product(characters, repeat=count_spaces)]
    for comb in combinations:
        equation = int(digits[0])
        for i in range(len(digits) - 1):
            if comb[i] == '+':
                equation += digits[i+1]
            if comb[i] == '*':
                equation *= digits[i+1]
        if equation == int(pair[0]):
            count += equation
            break
print(count)