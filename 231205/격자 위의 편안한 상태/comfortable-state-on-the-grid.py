def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

N, M = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for _ in range(M):
    r, c = tuple(map(int, input().split()))
    r, c = r-1, c-1
    arr_2d[r][c] = 1
    cnt = 0
    for dir_num in range(4):
        nr, nc = r + dxs[dir_num], c + dys[dir_num]
        if in_range(nr, nc) and arr_2d[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)