pairs, lines, = [], []
result, count = 0, 0
with open('5_data.txt', 'r') as file:
    for line in file:
        if '|' in line:
            pairs.append(line.strip('\n').split('|'))
        else:
            lines.append(line.strip('\n').split(','))

for line in lines:
    new_pairs = []
    for pair in pairs:
        previous = pair[0]
        next = pair[1]
        if previous in line and next in line:
            new_pairs.append([previous, next])
    round_first = True
    while count != len(new_pairs):
        count = 0
        for pair in new_pairs:
            previous = pair[0]
            next = pair[1]
            previous_index = line.index(previous)
            next_index = line.index(next)
            if previous_index > next_index:
                round_first = False
                line.remove(previous)
                line.insert(next_index, previous)
            else:
                count += 1
    if not round_first:
        result += int(line[len(line) // 2])

print(result)