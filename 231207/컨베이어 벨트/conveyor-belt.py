n, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(2)
]
grid[1].reverse()

def forward():
    tmp1 = grid[0][n-1]
    tmp2 = grid[1][0]
    for i in range(n-1, 0, -1):
        grid[0][i] = grid[0][i-1] 
    for i in range(0, n-1, 1):
        grid[1][i] = grid[1][i+1]
    grid[1][n-1] = tmp1
    grid[0][0] = tmp2

for _ in range(t):
    forward()
grid[1].reverse()

for i in range(2):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()