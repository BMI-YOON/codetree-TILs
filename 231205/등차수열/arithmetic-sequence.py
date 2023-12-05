n = int(input())
arr = list(map(int, input().split()))
max_val = 0
for i in range(min(arr), max(arr) + 1):
    cnt = 0
    for j in range(n):
        for k in range(j+1, n):
            if arr[j] - i == i - arr[k]:
                cnt += 1
    max_val = max(max_val, cnt)
print(max_val)