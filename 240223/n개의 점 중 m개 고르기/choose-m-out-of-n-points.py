import sys

n, m = tuple(map(int, input().split()))
arr = list()
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

def dist(dot1, dot2):
    x1, y1 = arr[dot1]
    x2, y2 = arr[dot2]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

grid = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        grid[i][j] = dist(i, j)

selected = list()
ans = sys.maxsize

def simulate(cur):
    global n, m, arr, grid, selected, ans

    if len(selected) == m:
        max_val = sys.maxsize 
        for i in range(len(selected)):
            for j in range(i+1, len(selected)):
                max_val = min(max_val, grid[selected[i]][selected[j]])
        ans = min(ans, max_val)
        return 
    
    if cur == n:
        return 

    simulate(cur+1)
    
    selected.append(cur)
    simulate(cur+1)
    selected.pop()

simulate(0)
print(ans)