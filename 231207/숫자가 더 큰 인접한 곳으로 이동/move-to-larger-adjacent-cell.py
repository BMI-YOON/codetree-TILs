n, r, c = tuple(map(int, input().split()))
r, c = r-1, c-1
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    return True

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
while True:
    print(grid[r][c], end = ' ')
    max_pos = (-1, -1)
    flag = 0
    for dx, dy in zip(dxs, dys):
        next_x, next_y = r + dx, c + dy 
        if in_range(next_x, next_y) and grid[next_x][next_y] > grid[r][c] and flag == 0:
            max_pos = (next_x, next_y)
            flag = 1
    r, c = max_pos
    if flag == 0:
        break