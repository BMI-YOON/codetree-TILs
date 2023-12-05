n = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
ans = 0
for i in range(0, n):
    for j in range(0, n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            if in_range(i+dx, j+dy) and arr_2d[i+dx][j+dy] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
print(ans)