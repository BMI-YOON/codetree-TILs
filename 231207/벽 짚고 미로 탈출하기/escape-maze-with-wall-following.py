N = int(input())
x, y = tuple(map(int, input().split()))
x, y = x-1, y-1
grid = [
    list(input())
    for _ in range(N)
]

start_x, start_y, z = x, y, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
t = 0
while True:
    next_x, next_y = x + dxs[z], y + dys[z]

    if next_x < 0 or next_x >= N:
        t += 1
        break 
    if next_y < 0 or next_y >= N:
        t += 1
        break

    if grid[next_x][next_y] == '#':
        z -= 1
        if z == -1:
            z = 3
    else:
        x, y = next_x, next_y
        t += 1
        z += 1
        if z == 4:
            z = 0
        '''
        next_x, next_y = x + dxs[z], y + dys[z]
        if grid[next_x][next_y] == '#':
            z -= 1
            if z == -1:
                z = 3
        else:
            x, y = next_x, next_y
            t += 1
        '''

    if x == start_x and y == start_y and z == 0:
        t = -1
        break

print(t)