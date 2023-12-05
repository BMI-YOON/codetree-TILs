N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i, N):
        cnt = 0
        mean_val = sum(arr[i : j+1]) / (j - i + 1)
        for k in range(i, j+1):
            if arr[k] == mean_val:
                cnt = 1
        ans += cnt 
print(ans)