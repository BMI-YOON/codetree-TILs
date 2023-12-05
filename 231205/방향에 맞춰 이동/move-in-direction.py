N = int(input())
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
x, y = 0, 0
for _ in range(N):
    direction, num = input().split()
    num = int(num)
    if direction == 'W':
        x, y = x + num * dx[0], y + num * dy[0]
    if direction == 'S':
        x, y = x + num * dx[1], y + num * dy[1]
    if direction == 'N':
        x, y = x + num * dx[2], y + num * dy[2]
    if direction == 'E':
        x, y = x + num * dx[3], y + num * dy[3]
print(x, y)