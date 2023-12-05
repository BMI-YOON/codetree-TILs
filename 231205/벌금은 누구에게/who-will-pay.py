N, M, K = tuple(map(int, input().split()))
arr = [0] * (N+1)
ans = -1
for _ in range(M):
    num = int(input())
    arr[num] += 1
    if arr[num] >= K:
        ans = num
        break
print(ans)