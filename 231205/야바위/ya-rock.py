N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

ans = 0
for i in range(1, 4):
    cur, cnt = i, 0
    for j in range(N):
        if arr[j][0] == cur:
            cur = arr[j][1]
        elif arr[j][1] == cur:
            cur = arr[j][0]
        if arr[j][2] == cur:
            cnt += 1
    ans = max(ans, cnt)
print(ans)