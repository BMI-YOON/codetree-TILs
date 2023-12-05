N, K = tuple(map(int, input().split()))
arr = [0] * 101
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    arr[b] += a 

ans = 0
for i in range(0, 101):
    sum = 0
    for j in range(max(0, i-K), min(100, i+K) +1):
        sum += arr[j]
    ans = max(ans, sum)
print(ans)