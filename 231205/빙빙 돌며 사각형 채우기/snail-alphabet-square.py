def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m 

n, m = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]
arr_2d[0][0] = 'A'

x, y, dir_num = 0, 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(2, n*m + 1):
    cur = arr_2d[x][y]
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr_2d[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    cur = chr(ord(cur) + 1)
    if cur == '[':
        cur = 'A'
    arr_2d[x][y] = cur 
    
for row in arr_2d:
    for elem in row:
        print(elem, end = ' ')
    print()