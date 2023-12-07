n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False

def find(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return (i, j)

dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]
def switch(x, y):
    next_x, next_y, max_val = -1, -1, -1
    for k in range(8):
        if in_range(x + dxs[k], y + dys[k]) and grid[x + dxs[k]][y + dys[k]] > max_val:
            max_val = grid[x + dxs[k]][y + dys[k]]
            next_x, next_y = x + dxs[k], y + dys[k]
    grid[x][y], grid[next_x][next_y] = grid[next_x][next_y], grid[x][y]

for _ in range(m):
    for num in range(1, n*n + 1):
        x, y = find(num)
        switch(x, y)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()