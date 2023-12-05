n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

ans = 100
for i in range(n):
    min_x, max_x = 101, 0
    for j in range(n):
        if j == i:
            continue
        min_x = min(min_x, arr[j][0])
        max_x = max(max_x, arr[j][1])
    ans = min(ans, max_x - min_x)
print(ans)