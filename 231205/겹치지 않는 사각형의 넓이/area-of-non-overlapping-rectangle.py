OFFSET = 1000
arr_2d = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]
for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1 + OFFSET, x2 + OFFSET):
        for j in range(y1 + OFFSET, y2 + OFFSET):
            arr_2d[i][j] = 1

x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1 + OFFSET, x2 + OFFSET):
    for j in range(y1 + OFFSET, y2 + OFFSET):
        arr_2d[i][j] = 0

cnt = 0
for row in arr_2d:
    for elem in row:
        if elem == 1:
            cnt += 1
print(cnt)