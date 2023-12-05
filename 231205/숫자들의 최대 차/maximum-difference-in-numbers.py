N, K = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0
for i in range(1, 10000-K+1):
    cnt = 0
    for j in range(N):
        if i <= arr[j] and arr[j] <= i+K:
            cnt += 1
    ans = max(ans, cnt)
print(ans)