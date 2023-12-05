N, M = tuple(map(int, input().split()))
arr_2d = [
    list(input())
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]
cnt = 0
for i in range(N):
    for j in range(M):
        for k in range(8):
            if not in_range(i + dxs[k], j + dys[k]):
                continue
            if not in_range(i + 2 * dxs[k], j + 2 * dys[k]):
                continue
            if arr_2d[i][j] == 'L' and arr_2d[i + dxs[k]][j + dys[k]] == 'E' and arr_2d[i + 2 * dxs[k]][j + 2* dys[k]] == 'E':
                cnt += 1
print(cnt)