import sys

n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(1, 10000 - k + 1):
    sum = 0
    for j in range(n):
        if arr[j] < i:
            sum += abs(i - arr[j])
        if i + k < arr[j]:
            sum += abs(arr[j] - i - k)
    ans = min(ans, sum)
print(ans)