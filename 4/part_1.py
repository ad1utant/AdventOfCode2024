tab, temp_tab = [],[]
count = 0
horizontal, vertical, diagonal_left, diagonal_right = None, None, None, None
with open('4_data.txt', 'r') as file:
    for line in file:
        for character in line:
            temp_tab.append(character)
        del temp_tab[-1]
        tab.append(temp_tab)
        temp_tab = []

for i in range(len(tab)):
    for j in range(len(tab[i])):
        if i < len(tab) - 3:
            vertical = tab[i][j] + tab[i+1][j] + tab[i+2][j] + tab[i+3][j]
        if j < len(tab[i]) - 3:
            horizontal = tab[i][j] + tab[i][j+1] + tab[i][j+2] + tab[i][j+3]
        if j < len(tab[i]) - 3 and i < len(tab) - 3:
            diagonal_right = tab[i][j] + tab[i+1][j+1] + tab[i+2][j+2] + tab[i+3][j+3]
        if j > 2 and i < len(tab) - 3:
            diagonal_left = tab[i][j] + tab[i+1][j-1] + tab[i+2][j-2] + tab[i+3][j-3]

        if vertical == "XMAS" or vertical == "SAMX":
            count += 1
        if horizontal == "XMAS" or horizontal == "SAMX":
            count += 1
        if diagonal_right == "XMAS" or diagonal_right == "SAMX":
            count += 1
        if diagonal_left == "XMAS" or diagonal_left == "SAMX":
            count += 1
        horizontal, vertical, diagonal_left, diagonal_right = None, None, None, None

print(count)