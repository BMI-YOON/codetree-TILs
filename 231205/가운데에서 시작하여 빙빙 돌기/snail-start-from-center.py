n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

x, y, dir_num = (n-1)//2, (n-1)//2, 0
arr_2d[x][y] = 1
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
cnt = 1
cur = 1
while True:
    for _ in range(cnt):
        if cur == n*n:
            break
        x, y = x + dxs[dir_num], y + dys[dir_num]
        cur += 1
        arr_2d[x][y] = cur
    if cur == n*n:
        break
    dir_num = (dir_num + 1) % 4
    for _ in range(cnt):
        if cur == n*n:
            break
        x, y = x + dxs[dir_num], y + dys[dir_num]
        cur += 1
        arr_2d[x][y] = cur
    if cur == n*n:
        break
    dir_num = (dir_num + 1) % 4
    cnt += 1

for row in arr_2d:
    for elem in row:
        print(elem, end = ' ')
    print()