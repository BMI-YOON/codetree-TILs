N = int(input())
arr = list(map(int, list(input())))

ans = 0
for i in range(N):
    if arr[i] == 1:
        continue
    arr[i] = 1
    last_idx = -1
    min_dist = 20
    for j in range(N):
        if last_idx >= 0 and arr[j] == 1:
            min_dist = min(min_dist, j - last_idx)
        if arr[j] == 1:
            last_idx = j
    ans = max(ans, min_dist)
    arr[i] = 0
print(ans)