def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N 

N, T = tuple(map(int, input().split()))
arr = list(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

x, y, dir_num = (N-1)//2, (N-1)//2, 0
ans = arr_2d[x][y]
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
for elem in arr:
    if elem == 'L':
        dir_num = (dir_num + 1) % 4
    if elem == 'R':
        dir_num = (dir_num -1 + 4) % 4
    if elem == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny 
            ans += arr_2d[x][y]
print(ans)