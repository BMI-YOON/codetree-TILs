from collections import deque

n, m = tuple(map(int, input().split()))
grid_input = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = list(map(int, input().split()))
grid = [
    [deque() for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        grid[i][j].append(grid_input[i][j])

def find(num):
    for i in range(n):
        for j in range(n):
            for k in range(len(grid[i][j])):
                if grid[i][j][k] == num:
                    return (i, j)

def find_max(i, j):
    max_i, max_j, max_val = -1, -1, -1
    for k in range(8):
        ni, nj = i + dxs[k], j + dys[k]
        if ni < 0 or ni >= n or nj < 0 or nj >= n:
            continue
        for l in range(len(grid[ni][nj])):
            if grid[ni][nj][l] > max_val:
                max_val = grid[ni][nj][l]
                max_i, max_j = ni, nj 
    return (max_i, max_j)

dxs, dys = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, 1, -1, 0, 1, -1]
for elem in arr:
    i, j = find(elem)
    temp_dq = deque()
    max_i, max_j = find_max(i, j)
    if max_i == -1 and max_j == -1:
        continue
    while True:
        temp = grid[i][j].pop()
        temp_dq.appendleft(temp)
        if temp == elem:
            break
    for k in range(len(temp_dq)):
        grid[max_i][max_j].append(temp_dq.popleft())

for i in range(n):
    for j in range(n):
        if len(grid[i][j]) == 0:
            print('None')
        else:
            for k in range(len(grid[i][j])-1, -1, -1):
                print(grid[i][j][k], end = ' ')
            print()