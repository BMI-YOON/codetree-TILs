N = int(input())
OFFSET = 100
arr_2d = [
[0 for _ in range(200)]
for _ in range(200)
]
for _ in range(N):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_2d[i][j] += 1
cnt = 0
for row in arr_2d:
    for elem in row:
        if elem > 0:
            cnt += 1
print(cnt)