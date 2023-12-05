N = int(input())
arr = [
    1 if int(input()) > 0 else -1
    for _ in range(N)
]

ans = cnt = 0
for i in range(N):
    if i >= 1 and arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)
print(ans)