n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for i in range(n):
    flag = 0
    for j in range(n-m+1):
        if m == 1:
            flag = 1
        for k in range(1, m):
            if arr[i][j+k] != arr[i][j]:
                break
            if k == m-1:
                flag = 1
    if flag == 1:
        cnt += 1
for j in range(n):
    flag = 0
    for i in range(n-m+1):
        if m == 1:
            flag = 1
        for k in range(1, m):
            if arr[i+k][j] != arr[i][j]:
                break
            if k == m-1:
                flag = 1
    if flag == 1:
        cnt += 1
print(cnt)