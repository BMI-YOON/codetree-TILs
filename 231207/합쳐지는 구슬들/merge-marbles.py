n, m, t = tuple(map(int, input().split()))
grid = [
    [[0, 0, 0] for _ in range(n)]
    for _ in range(n)
]
dir_mapper = {'U':0, 'R':1, 'L':2, 'D':3}
dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
for num in range(1, m+1):
    r, c, d, w = input().split()
    r = int(r) - 1
    c = int(c) - 1
    d = dir_mapper[d]
    w = int(w)
    grid[r][c][0] = w
    grid[r][c][1] = num
    grid[r][c][2] = d

def out_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

for _ in range(t):
    next_grid = [
        [[0, 0, 0] for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == [0, 0, 0]:
                continue
            w, num, d = grid[i][j][0], grid[i][j][1], grid[i][j][2]
            ni, nj = i + dxs[d], j + dys[d]
            if out_range(ni, nj):
                d = 3 - d 
                next_grid[i][j][0] += w
                if next_grid[i][j][1] < num:
                    next_grid[i][j][1] = num 
                    next_grid[i][j][2] = d
            else:
                next_grid[ni][nj][0] += w
                if next_grid[ni][nj][1] < num:
                    next_grid[ni][nj][1] = num
                    next_grid[ni][nj][2] = d 
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

ans_cnt, ans_w = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != [0, 0, 0]:
            ans_cnt += 1
            ans_w = max(ans_w, grid[i][j][0])
print(ans_cnt, ans_w)