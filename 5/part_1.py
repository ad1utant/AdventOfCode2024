pairs, lines, correct_lines = [], [], []
result, count = 0, 0
with open('5_data.txt', 'r') as file:
    for line in file:
        if '|' in line:
            pairs.append(line.strip('\n').split('|'))
        else:
            lines.append(line.strip('\n').split(','))

for line in lines:
    for pair in pairs:
        previous = pair[0]
        next = pair[1]
        if previous in line and next in line:
            previous_index = line.index(previous)
            next_index = line.index(next)
            if previous_index < next_index:
                count += 1
        else:
            count += 1
        if count == len(pairs):
            correct_lines.append(line)
    count = 0

for line in correct_lines:
    result += int(line[len(line)//2])
print(result)