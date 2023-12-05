N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

ans = 0
for i in range(N):
    cnt = 0
    for j in range(1, 1001):
        boolean = False
        for k in range(N):
            if k == i:
                continue
            if arr[k][0] <= j and j < arr[k][1]:
                boolean = True
        if boolean:
            cnt += 1
    ans = max(ans, cnt)
print(ans)