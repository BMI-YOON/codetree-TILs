n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            arr.append((i, j))
m = len(arr)

ans = 0

def in_range(x, y):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False 
    return True

def count():
    global n, grid, arr, m, ans
    cnt = 0
    cnt_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            dxs, dys = [-2, -1, 1, 2], [0, 0, 0, 0]
            if grid[i][j] == 1:
                for k in range(4):
                    x = i + dxs[k]
                    y = j + dys[k]
                    if in_range(x, y) and grid[x][y] == 0:
                        cnt_grid[x][y] = -1
            dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
            if grid[i][j] == 2:
                for k in range(4):
                    x = i + dxs[k]
                    y = j + dys[k]
                    if in_range(x, y) and grid[x][y] == 0:
                        cnt_grid[x][y] = -1
            dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]
            if grid[i][j] == 3:
                for k in range(4):
                    x = i + dxs[k]
                    y = j + dys[k]
                    if in_range(x, y) and grid[x][y] == 0:
                        cnt_grid[x][y] = -1
    for i in range(n):
        for j in range(n):
            if cnt_grid[i][j] == -1 or grid[i][j] > 0:
                cnt += 1
    ans = max(ans, cnt)  

def simulate(cur):
    global n, grid, arr, m, ans
    if cur == m:
        count() 
        return
    for k in range(1, 4):
        grid[arr[cur][0]][arr[cur][1]] = k
        simulate(cur+1)

simulate(0)
print(ans)