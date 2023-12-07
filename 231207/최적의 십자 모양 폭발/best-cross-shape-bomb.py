import copy

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def bomb(row, col):
    global grid, next_grid 
    next_grid = copy.deepcopy(grid)
    tmp = grid[row][col]
    for i in range(n):
        for j in range(n):
            if (i == row or j == col) and (abs(i-row) + abs(j-col) < tmp):
                next_grid[i][j] = 0
    tmp_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for col in range(n):
        tmp_row = n-1
        for row in range(n-1, -1, -1):
            if next_grid[row][col] != 0:
                tmp_grid[tmp_row][col] = next_grid[row][col]
                tmp_row -= 1
        for row in range(n):
            next_grid[row][col] = tmp_grid[row][col]

def count():
    global next_grid
    cnt = 0
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] == 0:
                continue
            if (i+1 < n and next_grid[i+1][j] == next_grid[i][j]):
                # and (i+2 >= n or next_grid[i+2][j] != next_grid[i][j]) and (i-1 < 0 or next_grid[i-1][j] != next_grid[i][j])
                cnt += 1
            if (j+1 < n and next_grid[i][j+1] == next_grid[i][j]):
                # and (j+2 >= n or next_grid[i][j+2] != next_grid[i][j]) and (j-1 < 0 or next_grid[i][j-1] != next_grid[i][j])
                cnt += 1
    return cnt

max_val = 0
for row in range(n):
    for col in range(n):
        bomb(row, col)
        max_val = max(max_val, count())
print(max_val)