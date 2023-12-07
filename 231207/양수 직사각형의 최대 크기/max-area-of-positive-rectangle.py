n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = -1
for i1 in range(n):
    for j1 in range(m):
        for i2 in range(i1, n):
            for j2 in range(j1, m):
                flag = 0
                for i in range(i1, i2+1):
                    for j in range(j1, j2+1):
                        if grid[i][j] <= 0:
                            flag = 1
                if flag == 0:
                    max_val = max(max_val, (i2 - i1 + 1) * (j2 - j1 + 1))
print(max_val)