n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def bomb(c):
    global grid
    c -= 1
    r = -1
    for i in range(n):
        if grid[i][c] != 0:
            r = i 
            break
    tmp = grid[r][c]
    if r != -1:
        for i in range(n):
            for j in range(n):
                if (i == r or j == c) and (abs(i - r) + abs(j - c) < tmp):
                    grid[i][j] = 0

def gravity():
    temp = [[0] * n for _ in range(n)]
    for col in range(n):
        temp_row = n-1
        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                temp[temp_row][col] = grid[row][col]
                temp_row -= 1
        for row in range(n):
            grid[row][col] = temp[row][col]

for _ in range(m):
    c = int(input())
    bomb(c)
    gravity()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()