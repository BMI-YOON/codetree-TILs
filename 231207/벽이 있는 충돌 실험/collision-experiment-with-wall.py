import copy

T = int(input())
dir_mapper = {'U':0, 'R':1, 'L':2, 'D':3}
dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

def in_range(x, y):
    global N
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False
    return True

for _ in range(T):
    N, M = tuple(map(int, input().split()))
    grid = [
        [[0, 0] for _ in range(N)]
        for _ in range(N)
    ]
    for _ in range(M):
        x, y, d = input().split()
        x = int(x) - 1
        y = int(y) - 1
        d = dir_mapper[d]
        grid[x][y] = [1, d]
    
    for _ in range(100):
        next_grid = [
            [[0, 0] for _ in range(N)]
            for _ in range(N)
        ]
        for i in range(N):
            for j in range(N):
                if grid[i][j][0] == 1:
                    ni, nj = i + dxs[grid[i][j][1]], j + dys[grid[i][j][1]]
                    if not in_range(ni, nj):
                        next_grid[i][j][0] += 1
                        next_grid[i][j][1] = 3 - grid[i][j][1]
                    else:
                        next_grid[ni][nj][0] += 1
                        next_grid[ni][nj][1] = grid[i][j][1]
        for i in range(N):
            for j in range(N):
                if next_grid[i][j][0] >= 2:
                    next_grid[i][j][0] = 0
                    next_grid[i][j][1] = 0
        for i in range(N):
            for j in range(N):
                grid[i][j] = next_grid[i][j]
        '''
        for i in range(N):
            for j in range(N):
                print(grid[i][j][0], end = ' ')
            print()
        print()
        '''

    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j][0] == 1:
                ans += 1
    print(ans)