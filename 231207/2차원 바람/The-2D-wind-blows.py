import copy

N, M, Q = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

for _ in range(Q):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    tmp = grid[r1][c1]
    for i in range(r1, r2):
        grid[i][c1] = grid[i+1][c1]
    for j in range(c1, c2):
        grid[r2][j] = grid[r2][j+1]
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i-1][c2]
    for j in range(c2, c1, -1):
        grid[r1][j] = grid[r1][j-1]
    grid[r1][c1+1] = tmp 

    new_grid = copy.deepcopy(grid)
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            sum, cnt = grid[i][j], 1
            dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
            for k in range(4):
                if 0 <= i + dxs[k] and i + dxs[k] < N and 0 <= j + dys[k] and j + dys[k] < M:
                    sum += grid[i+dxs[k]][j+dys[k]]
                    cnt += 1
            new_grid[i][j] = int(sum / cnt)       
    grid = copy.deepcopy(new_grid)

for i in range(N):
    for j in range(M):
        print(grid[i][j], end = ' ')
    print()