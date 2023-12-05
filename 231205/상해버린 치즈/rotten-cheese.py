N, M, D, S = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(M+1)]
    for _ in range(N+1)
]
arr = [0] * (N+1)
for _ in range(D):
    p, m, t = tuple(map(int, input().split()))
    arr_2d[p][m] = t 
for _ in range(S):
    p, t = tuple(map(int, input().split()))
    arr[p] = t

cnt = [0] * (N+1)

for j in range(1, M+1):
    boolean = True
    for i in range(1, N+1):
        if arr[i] == 0:
            continue
        elif arr_2d[i][j] == 0:
            boolean = False
        elif arr_2d[i][j] >= arr[i]:
            boolean = False
    if boolean:
        for i in range(1, N+1):
            if arr_2d[i][j] != 0:
                cnt[i] = 1
print(sum(cnt))