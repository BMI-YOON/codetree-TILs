N, M = tuple(map(int, input().split()))
arr_A = [0] * 10000001
arr_B = [0] * 10000001

cur = 0
for _ in range(N):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(1, t + 1):
            arr_A[cur + i] = arr_A[cur] + i
        cur += t 
    else:
        for i in range(1, t + 1):
            arr_A[cur + i] = arr_A[cur] - i
        cur += t

cur = 0
for _ in range(M):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(1, t + 1):
            arr_B[cur + i] = arr_B[cur] + i
        cur += t
    else:
        for i in range(1, t + 1):
            arr_B[cur + i] = arr_B[cur] - i
        cur += t

for i in range(1, cur + 1):
    if arr_A[i] == arr_B[i]:
        print(i)
        break
    if i == cur:
        print(-1)