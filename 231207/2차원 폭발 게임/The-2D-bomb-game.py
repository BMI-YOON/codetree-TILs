import copy

N, M, K = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

def bomb():
    global N, M, K, grid
    flag = 0
    for col in range(N):
        cur_num, cur_cnt, start_idx = -1, 0, -1
        for row in range(N):
            if grid[row][col] == 0:
                continue
            if grid[row][col] == cur_num:
                cur_cnt += 1
                if cur_cnt == M:
                    flag = 1
                    for r in range(start_idx, row + 1):
                        grid[r][col] = 0
                if cur_cnt > M:
                    grid[row][col] = 0                    
            else:
                cur_num = grid[row][col]
                cur_cnt = 1 
                start_idx = row
    return flag 

def gravity():
    global N, M, K, grid
    next_grid = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]
    for col in range(N):
        tmp_row = N-1
        for row in range(N-1, -1, -1):
            if grid[row][col] != 0:
                next_grid[tmp_row][col] = grid[row][col]
                tmp_row -= 1
        for row in range(N):
            grid[row][col] = next_grid[row][col]

def rotation():
    global N, M, K, grid
    next_grid = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]
    for row in range(N):
        for col in range(N):
            next_grid[col][N-1-row] = grid[row][col] 
    grid = copy.deepcopy(next_grid)

'''
bomb()
gravity()
bomb()
rotation()
for i in range(N):
    for j in range(N):
        print(grid[i][j], end = ' ')
    print() 
'''

if M == 1:
    print(0)
else:
    for _ in range(K):
        while True:
            if bomb() == 1:
                gravity()
            else:
                break

        rotation()
        gravity()
    while True:
        if bomb() == 1:
            gravity()
        else:
            break
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                cnt += 1
    print(cnt)