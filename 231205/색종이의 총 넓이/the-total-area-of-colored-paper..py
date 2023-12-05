OFFSET = 100
arr_2d = [
    [0 for _ in range(200)]
    for _ in range(200)
]

N = int(input())
for _ in range(N):
    x, y = tuple(map(int, input().split()))
    for i in range(x + OFFSET, x + OFFSET + 8):
        for j in range(y + OFFSET, y + OFFSET + 8):
            arr_2d[i][j] = 1
cnt = 0
for row in arr_2d:
    for elem in row:
        if elem == 1:
            cnt += 1
print(cnt)