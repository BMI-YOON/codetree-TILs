def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

def direction(cur_dir, mirror):
    if cur_dir == 0:
        if mirror == '/':
            return 1
        else:
            return 3
    elif cur_dir == 1:
        if mirror == '/':
            return 0
        else:
            return 2
    elif cur_dir == 2:
        if mirror == '/':
            return 3
        else:
            return 1
    else:
        if mirror == '/':
            return 2
        else:
            return 0

N = int(input())
arr_2d = [
    list(input())
    for _ in range(N)
]
K = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

if (K - 1) // N < 1:
    x, y = 0, (K % N) - 1
    cur_dir = direction(0, arr_2d[x][y])
elif (K - 1) // N < 2:
    x, y = (K % N) - 1, N - 1
    cur_dir = direction(1, arr_2d[x][y])
elif (K - 1) // N < 3:
    x, y = N - 1, N - (K % N)
    cur_dir = direction(2, arr_2d[x][y])
else:
    x, y = N - (K % N), 0
    cur_dir = direction(3, arr_2d[x][y])
cnt = 1
while True:
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if not in_range(nx, ny):
        print(cnt)
        break
    cnt += 1
    x, y = nx, ny 
    cur_dir = direction(cur_dir, arr_2d[x][y])