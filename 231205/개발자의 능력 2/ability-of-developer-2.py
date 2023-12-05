import sys
arr = list(map(int, input().split()))
sum = sum(arr)
ans = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(6):
            if k == i or k == j:
                continue
            for l in range(k+1, 6):
                if l == i or l == j:
                    continue
                min_val = min(arr[i] + arr[j], arr[k] + arr[l], sum - arr[i] - arr[j] - arr[k] - arr[l])
                max_val = max(arr[i] + arr[j], arr[k] + arr[l], sum - arr[i] - arr[j] - arr[k] - arr[l])
                ans = min(ans, max_val - min_val)
print(ans)