import sys 

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def f(i1, j1, i2, j2, i3, j3, i4, j4):
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            if i3 <= i and i <= i4 and j3 <= j and j <= j4:
                return False 
    return True

max_val = -sys.maxsize
for i1 in range(n):
    for j1 in range(m):
        for i2 in range(i1, n):
            for j2 in range(j1, m):
                for i3 in range(n):
                    for j3 in range(m):
                        for i4 in range(i3, n):
                            for j4 in range(j3, m):
                                if not f(i1, j1, i2, j2, i3, j3, i4, j4):
                                    continue
                                else:
                                    sum = 0
                                    for i in range(i1, i2+1):
                                        for j in range(j1, j2+1):
                                            sum += grid[i][j]
                                    for i in range(i3, i4+1):
                                        for j in range(j3, j4+1):
                                            sum += grid[i][j]                                 
                                    max_val = max(max_val, sum)
print(max_val)