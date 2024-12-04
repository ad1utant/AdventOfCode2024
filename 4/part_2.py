tab, temp_tab = [],[]
tab_x = [['M','M','S','S' ],['M','S','M','S'],['S','M','S','M'],['S','S','M','M']]
count = 0
with open('4_data.txt', 'r') as file:
    for line in file:
        for character in line:
            temp_tab.append(character)
        del temp_tab[-1]
        tab.append(temp_tab)
        temp_tab = []

for i in range(len(tab)):
    for j in range(len(tab[i])):
        if tab[i][j] == 'A' and i < len(tab) - 1 and j > 0 and i > 0 and j < len(tab[i]) - 1:
            a1, a2, a3, a4 = tab[i-1][j-1], tab[i-1][j+1], tab[i+1][j-1], tab[i+1][j+1]
            temp_tab = [a1, a2, a3, a4]
            for option in tab_x:
                if option == temp_tab:
                    count += 1
            temp_tab = []

print(count)