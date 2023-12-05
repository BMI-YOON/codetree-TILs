N = int(input())
arr = list(map(int, list(input())))

start_idx, last_idx, cur, max_dist, min_dist = -1, -1, -1, 0, 1001
for i in range(N):
    if arr[i] == 1:
        if cur == -1:
            start_idx = i
            cur = i 
        else:
            max_dist = max(max_dist, i - cur)
            min_dist = min(min_dist, i - cur)
            cur = i
            last_idx = i

ans = (min(max_dist // 2, min_dist))
ans = min(ans, start_idx - 0)
ans = min(ans, N-1 - last_idx)

if last_idx == -1:
    print(max(start_idx - 0, N-1 - start_idx))
elif min_dist < max_dist // 2:
    print(min_dist)
else:
    if start_idx - 0 > min_dist or N-1 - last_idx > min_dist:
        print(min_dist)
    else:
        ans = max(max_dist // 2, start_idx - 0)
        ans = max(ans, N-1 - last_idx)
        print(ans)