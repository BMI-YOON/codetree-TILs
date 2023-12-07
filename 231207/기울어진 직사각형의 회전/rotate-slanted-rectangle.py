n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c, m1, m2, m3, m4, dir = tuple(map(int, input().split()))
r, c = r-1, c-1

tmp = grid[r][c]
cur_r, cur_c = r, c 
if dir == 0:
    for _ in range(m4):
        grid[cur_r][cur_c] = grid[cur_r-1][cur_c-1]
        cur_r -= 1
        cur_c -= 1
    for _ in range(m3):
        grid[cur_r][cur_c] = grid[cur_r-1][cur_c+1]
        cur_r -= 1
        cur_c += 1
    for _ in range(m2):
        grid[cur_r][cur_c] = grid[cur_r+1][cur_c+1]
        cur_r += 1
        cur_c += 1
    for _ in range(m1):
        grid[cur_r][cur_c] = grid[cur_r+1][cur_c-1]
        cur_r += 1
        cur_c -= 1
    grid[r-1][c+1] = tmp 
else:
    for _ in range(m1):
        grid[cur_r][cur_c] = grid[cur_r-1][cur_c+1]
        cur_r -= 1
        cur_c += 1
    for _ in range(m2):
        grid[cur_r][cur_c] = grid[cur_r-1][cur_c-1]
        cur_r -= 1
        cur_c -= 1
    for _ in range(m3):
        grid[cur_r][cur_c] = grid[cur_r+1][cur_c-1]
        cur_r += 1
        cur_c -= 1
    for _ in range(m4):
        grid[cur_r][cur_c] = grid[cur_r+1][cur_c+1]
        cur_r += 1
        cur_c += 1
    grid[r-1][c-1] = tmp 

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()