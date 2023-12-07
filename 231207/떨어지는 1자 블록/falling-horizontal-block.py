n, m, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
k -= 1

i = -1
while i < n - 1:
    flag = 0
    for j in range(k, k+m):
        if grid[i+1][j] == 1:
            flag = 1
    if flag == 0:
        i += 1
        continue
    else:
        break
for j in range(k, k+m):
    grid[i][j] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()