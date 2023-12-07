n, m, t, k = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
dir_mapper = {'U':0, 'D':3, 'R':1, 'L':2}
for i in range(m):
    r, c, d, v = input().split()
    grid[int(r)-1][int(c)-1].append((i+1, dir_mapper[d], int(v)))

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
for _ in range(t):
    next_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) == 0:
                continue
            for s in range(len(grid[i][j])):
                cur_i, cur_j, cur_d = i, j, grid[i][j][s][1]
                for _ in range(grid[i][j][s][2]):
                    if not in_range(cur_i + dxs[cur_d], cur_j + dys[cur_d]):
                        cur_d = 3 - cur_d
                    cur_i += dxs[cur_d]
                    cur_j += dys[cur_d]
                next_grid[cur_i][cur_j].append((grid[i][j][s][0], cur_d, grid[i][j][s][2]))
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) > k:
                next_grid[i][j].sort(key = lambda x: (-x[2], -x[0]))
                for _ in range(len(next_grid[i][j]) - k):
                    next_grid[i][j].pop()
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])
print(ans)