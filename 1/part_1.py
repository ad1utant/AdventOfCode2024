X,Y = [],[]
count = 0

with open('1_data.txt', 'r') as file:
    for line in file:
        X.append(int(line[0:5]))
        Y.append(int(line[8:13]))

while X and Y:
    mini_x = min(X)
    mini_y = min(Y)
    if mini_x > mini_y:
        count += mini_x - mini_y
    if mini_y > mini_x:
        count += mini_y - mini_x
    X.remove(mini_x)
    Y.remove(mini_y)

print(count)