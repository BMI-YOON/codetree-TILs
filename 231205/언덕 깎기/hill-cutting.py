import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = sys.maxsize
for i in range(84):
    cnt = 0
    for j in range(N):
        if arr[j] < i:
            cnt += (i - arr[j]) ** 2
        if i + 17 < arr[j]:
            cnt += (i + 17 - arr[j]) ** 2
    ans = min(ans, cnt)
print(ans)