n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c= tuple(map(int, input().split()))
r, c = r-1, c-1

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
for idx in range(4):
    for k in range(1, grid[r][c]):
        x = r + dxs[idx] * k
        y = c + dys[idx] * k
        if 0 <= x and x < n and 0 <= y and y < n:
            grid[x][y] = 0
grid[r][c] = 0

for j in range(n):
    tmp_arr = []
    for i in range(n):
        if grid[i][j] > 0:
            tmp_arr.append(grid[i][j])
    for i in range(n-len(tmp_arr)):
        grid[i][j] = 0
    for i in range(n-len(tmp_arr), n):
        grid[i][j] = tmp_arr[i-n+len(tmp_arr)]

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()