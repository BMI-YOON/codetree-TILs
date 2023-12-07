N, M, K = tuple(map(int, input().split()))
grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]
grid [0][0] = 2
for _ in range(M):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1
    grid[x][y] = -1

dir_mapper = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
head_x, head_y = (0, 0)
tail_x, tail_y = (0, 0)
t = 0
flag = 0
for _ in range(K):
    if flag == 1:
        break
    d, p = input().split()
    p = int(p)
    for _ in range(p):
        '''
        for xxx in range(N):
            for yyy in range(N):
                print(grid[xxx][yyy], end = ' ')
            print()
        print()
        '''
        next_x, next_y = head_x + dxs[dir_mapper[d]], head_y + dys[dir_mapper[d]]
        t += 1
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
            flag = 1
            break
        elif grid[next_x][next_y] >= 2 and not (next_x == tail_x and next_y == tail_y):
            flag = 1
            break
        elif grid[next_x][next_y] == -1:
            for i in range(N):
                for j in range(N):
                    if grid[i][j] >= 2:
                        grid[i][j] += 1
            grid[next_x][next_y] = 2
            head_x, head_y = next_x, next_y
        else:
            for idx in range(4):
                if tail_x == head_x and tail_y == head_y:
                    grid[tail_x][tail_y] = 0
                    tail_x, tail_y = next_x, next_y
                    break
                elif 0 <= tail_x + dxs[idx] and tail_x + dxs[idx] < N and 0 <= tail_y + dys[idx] and tail_y + dys[idx] < N and grid[tail_x + dxs[idx]][tail_y + dys[idx]] == grid[tail_x][tail_y] - 1:
                    grid[tail_x][tail_y] = 0
                    tail_x, tail_y = tail_x + dxs[idx], tail_y + dys[idx]
                    break
            for i in range(N):
                for j in range(N):
                    if grid[i][j] >= 2:
                        grid[i][j] += 1
            grid[next_x][next_y] = 2
            head_x, head_y = next_x, next_y
print(t)