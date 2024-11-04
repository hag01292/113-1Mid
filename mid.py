#a
map = [[0 for _ in range(10)] for _ in range(10)]

#b
rowMap = [0]*10

#c
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

#d
for index in rowMap:
    row = index // 10
    col = index % 10
    map[row][col] = "*"

#e
def is_valid(x,y):
    return 0 <= x < 10 and 0 <= y < 10
   

for i in range(10):
        for j in range (10):
            if map[i][j] == '*':
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy 
                        if is_valid(ni,nj) and map[ni][nj] != '*':
                            map[ni][nj] += 1
for i in range(10):
    for j in range(10):
        if map[row][col] == '0':
            map[row][col] = ' '                      

for row in map:                        
    print(" | ".join(str(cell) for cell in row))
    print("-" * (4 * 10 - 1))
