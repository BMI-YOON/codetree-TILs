OFFSET = 100
arr_2d = [
    [0 for _ in range(200)]
    for _ in range(200)
]
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    if i % 2 == 0:
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr_2d[j][k] = -1
    else:
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr_2d[j][k] = 1

cnt = 0
for row in arr_2d:
    for elem in row:
        if elem == 1:
            cnt += 1
print(cnt)