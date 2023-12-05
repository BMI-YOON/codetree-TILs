arr = list(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
x, y, dir_num, ans = 0, 0, 3, -1
for i in range(len(arr)):
    if arr[i] == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    if arr[i] == 'R':
        dir_num = (dir_num + 1) % 4
    if arr[i] == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    if x == 0 and y == 0:
        ans = i + 1
        break
print(ans)