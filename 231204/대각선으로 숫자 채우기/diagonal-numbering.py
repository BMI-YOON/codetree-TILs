n, m = tuple(map(int, input().split()))
num = 1
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for cnt in range(0, n-1+m-1+1):
    for j in range(cnt, -1, -1):
        if (cnt - j) < n and j < m:
            arr[cnt - j][j] = num 
            num += 1

for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()