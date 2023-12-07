import copy

n, m, r, c = tuple(map(int, input().split()))
r, c = r-1, c-1
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

grid[r][c] = 1
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
for t in range(m):
    tmp_grid = copy.deepcopy(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for idx in range(4):
                    if 0 <= i + dxs[idx] * (2**t) < n and 0 <= j + dys[idx] * (2**t) < n:
                        tmp_grid[i + dxs[idx] * (2**t)][j + dys[idx] * (2**t)] = 1
    grid = copy.deepcopy(tmp_grid)

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += grid[i][j]
print(cnt)