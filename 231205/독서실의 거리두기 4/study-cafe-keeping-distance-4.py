N = int(input())
arr = list(map(int, list(input())))

def f():
    min_dist = 100
    last_idx = -1
    for i in range(N):
        if last_idx >=0 and arr[i] == 1:
            min_dist = min(min_dist, i - last_idx)
        if arr[i] == 1:
            last_idx = i
    return min_dist

ans = 0
for i in range(N):
    if arr[i] == 1:
        continue
    for j in range(i+1, N):
        if arr[j] == 1:
            continue
        arr[i], arr[j] = 1, 1
        ans = max(ans, f())
        arr[i], arr[j] = 0, 0
print(ans)