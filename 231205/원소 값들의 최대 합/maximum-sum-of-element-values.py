n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    cur = i
    sum = arr[cur]
    for _ in range(m - 1):
        cur = arr[cur] - 1
        sum += arr[cur]
    ans = max(ans, sum)
print(ans)