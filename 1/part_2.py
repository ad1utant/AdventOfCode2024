X,Y = [],[]
count = 0

with open('1_data.txt', 'r') as file:
    for line in file:
        X.append(int(line[0:5]))
        Y.append(int(line[8:13]))

for item in X:
    count += item * Y.count(item)

print(count)