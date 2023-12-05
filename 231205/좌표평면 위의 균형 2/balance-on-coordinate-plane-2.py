N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

M = 101
for i in range(1, 51):
    for j in range(1, 51):
        cnt = [0, 0, 0, 0]
        for k in range(N):
            if arr[k][0] < 2 * i and arr[k][1] < 2 * j:
                cnt[0] += 1
            elif arr[k][0] > 2 * i and arr[k][1] < 2 * j:
                cnt[1] += 1
            elif arr[k][0] < 2 * i and arr[k][1] > 2 * j:
                cnt[2] += 1
            else:
                cnt[3] += 1
        M = min(M, max(cnt))
print(M)