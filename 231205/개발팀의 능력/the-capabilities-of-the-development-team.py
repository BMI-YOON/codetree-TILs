import sys
arr = list(map(int, input().split()))
sum = sum(arr)
ans = sys.maxsize
flag = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(5):
            if k == i or k == j:
                continue
            for l in range(k+1, 5):
                if l == i or l == j:
                    continue
                if (arr[i] + arr[j]) == (arr[k] + arr[l]) or (arr[k] + arr[l]) == (sum - arr[i] - arr[j] - arr[k] - arr[l]) or (sum - arr[i] - arr[j] - arr[k] - arr[l]) == (arr[i] + arr[j]):
                    continue
                min_val = min(arr[i] + arr[j], arr[k] + arr[l], sum - arr[i] - arr[j] - arr[k] - arr[l])
                max_val = max(arr[i] + arr[j], arr[k] + arr[l], sum - arr[i] - arr[j] - arr[k] - arr[l])
                ans = min(ans, max_val - min_val)
                flag = 1
if flag == 0:
    print(-1)
else:
    print(ans)