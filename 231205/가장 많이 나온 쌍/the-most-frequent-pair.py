n, m = tuple(map(int, input().split()))
arr = []
for _ in range(m):
    arr.append(tuple(map(int, input().split())))

ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cnt = 0
        for a, b in arr:
            if i == a and j == b:
                cnt += 1
            if i == b and j == a:
                cnt += 1
        ans = max(ans, cnt)
print(ans)