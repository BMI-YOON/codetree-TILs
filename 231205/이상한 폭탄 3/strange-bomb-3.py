N, K = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))

ans, max_val = 0, 1
for i in range(1, 1000000+1):
    cnt, last_idx, last_bomb = 0, -1, 0
    for j in range(N):
        if last_idx >= 0 and arr[j] == i:
            if j - last_idx <= K:
                if last_bomb == 1:
                    cnt += 1
                else:
                    cnt += 2
                last_bomb = 1
            else:
                last_bomb = 0
        if arr[j] == i:
            last_idx = j
    if cnt >= max_val:
        ans = i 
        max_val = cnt 
print(ans)