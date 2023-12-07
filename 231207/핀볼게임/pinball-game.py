n = int(input())
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

def direction(cur_dir, wall):
    if cur_dir == 0 and wall == 1:
        return 1
    if cur_dir == 0 and wall == 2:
        return 3
    if cur_dir == 2 and wall == 1:
        return 3
    if cur_dir == 2 and wall == 2:
        return 1
    if cur_dir == 1 and wall == 1:
        return 0
    if cur_dir == 1 and wall == 2:
        return 2
    if cur_dir == 3 and wall == 1:
        return 2
    if cur_dir == 3 and wall == 2:
        return 0
    return cur_dir

cur_x, cur_y, cur_dir = -1, -1, -1
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
ans = 0
for i in range(n):
    cur_x, cur_y, cur_dir, cnt = i, 0, 0, 1
    while in_range(cur_x, cur_y):
        cur_dir = direction(cur_dir, grid[cur_x][cur_y])
        cur_x += dxs[cur_dir]
        cur_y += dys[cur_dir]
        cnt += 1
    ans = max(ans, cnt)    
for i in range(n):
    cur_x, cur_y, cur_dir, cnt = i, n-1, 2, 1
    while in_range(cur_x, cur_y):
        cur_dir = direction(cur_dir, grid[cur_x][cur_y])
        cur_x += dxs[cur_dir]
        cur_y += dys[cur_dir]
        cnt += 1
    ans = max(ans, cnt) 
for j in range(n):
    cur_x, cur_y, cur_dir, cnt = n-1, j, 1, 1
    while in_range(cur_x, cur_y):
        cur_dir = direction(cur_dir, grid[cur_x][cur_y])
        cur_x += dxs[cur_dir]
        cur_y += dys[cur_dir]
        cnt += 1
    ans = max(ans, cnt) 
for j in range(n):
    cur_x, cur_y, cur_dir, cnt = 0, j, 3, 1
    while in_range(cur_x, cur_y):
        cur_dir = direction(cur_dir, grid[cur_x][cur_y])
        cur_x += dxs[cur_dir]
        cur_y += dys[cur_dir]
        cnt += 1
    ans = max(ans, cnt) 

print(ans)