__author__ = 'Sawl_Stone'

def found_oazis(map):
    count = 0
    for i in range(0, len(map)):  # i - row
        for j in range(0, len(map[i])): #j - col
            if map[i][j] == 1:
                count += 1
                area(map, i ,j)
    return count

def area(map, i, j):
    map[i][j] = 2
    if j-1 >= 0 and map[i][j-1] == 1:
        area(map, i, j-1)
    if j+1 < len(map[i]) and map[i][j+1] == 1:
        area(map, i, j+1)
    if i-1 >= 0 and map[i-1][j] == 1:
        area(map, i-1, j)
    if i+1 < len(map) and map[i+1][j] == 1:
        area(map, i+1, j)


def main():
    map = [[0,1,1,0], [0,0,0,0], [1,0,0,0], [0,0,0,1]]
    count = found_oazis(map)
    print(count)

main()