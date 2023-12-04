n, m = tuple(map(int, input().split()))
num = 0
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = num 
            num += 1
    else:
        for i in range(n-1, -1, -1):
            arr[i][j] = num 
            num += 1

for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()