grid = [
    list(map(int, input().split()))
    for _ in range(4)
]
dir = input()

if dir == 'L':
    tmp = [
        [0] * 4 
        for _ in range(4)
        ]
    for i in range(4):
        tmp_j = -1
        cur_num, cur_cnt = -1, 0
        for j in range(4):
            if grid[i][j] != 0:
                if grid[i][j] == cur_num:
                    cur_cnt += 1
                    if cur_cnt <= 2:
                        tmp[i][tmp_j] += grid[i][j]
                    else:
                        cur_cnt = 1
                        tmp_j += 1
                        tmp[i][tmp_j] += grid[i][j]
                else:
                    cur_num, cur_cnt = grid[i][j], 1
                    tmp_j += 1
                    tmp[i][tmp_j] += grid[i][j]
elif dir == 'R':
    tmp = [
        [0] * 4 
        for _ in range(4)
        ]
    for i in range(4):
        tmp_j = 4
        cur_num, cur_cnt = -1, 0
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                if grid[i][j] == cur_num:
                    cur_cnt += 1
                    if cur_cnt <= 2:
                        tmp[i][tmp_j] += grid[i][j]
                    else:
                        cur_cnt = 1
                        tmp_j -= 1
                        tmp[i][tmp_j] += grid[i][j]
                else:
                    cur_num, cur_cnt = grid[i][j], 1
                    tmp_j -= 1
                    tmp[i][tmp_j] += grid[i][j]
elif dir == 'U':
    tmp = [
        [0] * 4 
        for _ in range(4)
        ]
    for j in range(4):
        tmp_i = -1
        cur_num, cur_cnt = -1, 0
        for i in range(4):
            if grid[i][j] != 0:
                if grid[i][j] == cur_num:
                    cur_cnt += 1
                    if cur_cnt <= 2:
                        tmp[tmp_i][j] += grid[i][j]
                    else:
                        cur_cnt = 1
                        tmp_i += 1
                        tmp[tmp_i][j] += grid[i][j]
                else:
                    cur_num, cur_cnt = grid[i][j], 1
                    tmp_i += 1
                    tmp[tmp_i][j] += grid[i][j]
else:
    tmp = [
        [0] * 4 
        for _ in range(4)
        ]
    for j in range(4):
        tmp_i = 4
        cur_num, cur_cnt = -1, 0
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                if grid[i][j] == cur_num:
                    cur_cnt += 1
                    if cur_cnt <= 2:
                        tmp[tmp_i][j] += grid[i][j]
                    else:
                        cur_cnt = 1
                        tmp_i -= 1
                        tmp[tmp_i][j] += grid[i][j]
                else:
                    cur_num, cur_cnt = grid[i][j], 1
                    tmp_i -= 1
                    tmp[tmp_i][j] += grid[i][j]

for i in range(4):
    for j in range(4):
        print(tmp[i][j], end = ' ')
    print()