OFFSET = 1000
arr_2d = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1 + OFFSET, x2 + OFFSET):
    for j in range(y1 + OFFSET, y2 + OFFSET):
        arr_2d[i][j] = 1

x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1 + OFFSET, x2 + OFFSET):
    for j in range(y1 + OFFSET, y2 + OFFSET):
        arr_2d[i][j] = 0

cnt = 0
x1 = y1 = 2001
x2 = y2 = -1
for i in range(2000):
    for j in range(2000):
        if arr_2d[i][j] == 1:
            if i < x1:
                x1 = i 
            if j < y1: 
                y1 = j
            if i > x2:
                x2 = i 
            if j > y2:
                y2 = j
if x1 == 2001 or y1 == 2001 or x2 == -1 or y2 == -1:
    print(0)
else:
    print((x2 - x1 + 1) * (y2 - y1 + 1))