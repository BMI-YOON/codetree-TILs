N, K = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = -1
for i in range(N):
    for j in range(i+1, N):
        if arr[i] == arr[j] and (j - i) <= K:
            ans = max(ans, arr[i])
print(ans)