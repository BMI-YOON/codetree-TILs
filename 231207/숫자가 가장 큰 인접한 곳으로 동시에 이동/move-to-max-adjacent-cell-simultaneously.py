import copy

n, m, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    cnt[r-1][c-1] = 1

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(t):
    next_cnt = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for x in range(n):
        for y in range(n):
            if cnt[x][y] == 1:
                next_x, next_y, max_val = -1, -1, -1
                for k in range(4):
                    if x + dxs[k] < 0 or x + dxs[k] >= n:
                        continue
                    if y + dys[k] < 0 or y + dys[k] >= n:
                        continue
                    if grid[x + dxs[k]][y + dys[k]] > max_val:
                        max_val = grid[x + dxs[k]][y + dys[k]]
                        next_x, next_y = x + dxs[k], y + dys[k]
                next_cnt[next_x][next_y] += 1
    for x in range(n):
        for y in range(n):
            if next_cnt[x][y] >= 2:
                next_cnt[x][y] = 0
    cnt = copy.deepcopy(next_cnt)

ans = 0
for i in range(n):
    for j in range(n):
        if cnt[i][j] == 1:
            ans += 1
print(ans)