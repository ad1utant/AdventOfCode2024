pairs, lines, correct_lines = [], [], []
result, count = 0, 0
with open('5_test_data.txt', 'r') as file:
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
            lines.remove(line)
    count = 0

def transformation(line, pairs):
    code = []
    new_pairs = []
    for pair in pairs:
        if pair[0] in code and pair[1] in line:
            new_pairs.append(pair)
            if pair[0] not in code:
                code.append(pair[0])
            if pair[1] not in code:
                code.append(pair[1])
    print(f'line{line}')
    print(f'code{code}')
    count = 0
    while count != len(pairs):
        for pair in new_pairs:
            previous = pair[0]
            next = pair[1]
            previous_index = line.index(previous)
            next_index = line.index(next)
            if previous_index > next_index:
                code.remove(next)
                code.insert(previous_index, next)
                continue
            count += 1
        if count == len(pairs):
            break
        count = 0
    return code

for line in lines:
    print(transformation(line,pairs))
