N = int(input())
arr = list(map(int, list(input())))

start_idx, last_idx, cur, max_dist, min_dist = -1, -1, -1, 0, 1001
for i in range(N):
    if arr[i] == 1:
        if cur == -1:
            cur = i 
        else:
            max_dist = max(max_dist, i - cur)
            min_dist = min(min_dist, i - cur)
            cur = i

print(min(max_dist // 2, min_dist))