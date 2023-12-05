N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0
for i in range(1, 1001):
    cnt, cur = 0, 0
    for j in range(N):
        if arr[j] > i and cur == 0:
            cnt += 1
            cur = 1
        if arr[j] <= i:
            cur = 0
    ans = max(ans, cnt)
print(ans)