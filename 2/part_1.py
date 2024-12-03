count = 0

with open('2_data.txt', 'r') as file:
    for line in file:
        tab = list(map(int, line.split()))
        count_increasing, count_decreasing = 0, 0
        for i in range(len(tab) - 1):
            if tab[i+1] > tab[i] and tab[i+1] - tab[i] in [1,2,3]:
                count_increasing += 1
        for i in range(len(tab) - 1):
            if tab[i+1] < tab[i] and tab[i] - tab[i+1] in [1,2,3]:
                count_decreasing += 1
        if len(tab)-1 == count_decreasing or len(tab)-1 == count_increasing:
            count += 1
print(count)