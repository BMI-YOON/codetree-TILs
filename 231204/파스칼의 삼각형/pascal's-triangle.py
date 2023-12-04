n = int(input())
arr = [
    [1 for _ in range(n)]
    for _ in range(n)
]
for i in range(1, n):
    for j in range(1, n):
        if i > j:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(n):
    for j in range(n):
        if i >= j:
            print(arr[i][j], end = ' ')
    print()