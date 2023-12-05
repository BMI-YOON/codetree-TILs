arr = list(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = 3
for elem in arr:
    if elem == 'L':
        direction = (direction - 1 + 4) % 4
    if elem == 'R':
        direction = (direction + 1) % 4
    if elem == 'F':
        x, y = x + dx[direction], y + dy[direction]
print(x, y)