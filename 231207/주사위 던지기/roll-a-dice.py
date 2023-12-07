n, m, r, c = tuple(map(int, input().split()))
r, c = r-1, c-1
arr = input().split()
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cur, cur_L, cur_R, cur_U, cur_D = 6, 4, 3, 5, 2
grid[r][c] = cur
for elem in arr:
    if elem == 'L':
        if c-1 < 0:
            continue
        cur, cur_L, cur_R, cur_U, cur_D = cur_L, 7-cur, cur, cur_U, cur_D
        c -= 1
        grid[r][c] = cur 
    elif elem == 'R':
        if c+1 >= n:
            continue 
        cur, cur_L, cur_R, cur_U, cur_D = cur_R, cur, 7-cur, cur_U, cur_D 
        c += 1
        grid[r][c] = cur 
    elif elem == 'U':
        if r-1 < 0:
            continue 
        cur, cur_L, cur_R, cur_U, cur_D = cur_U, cur_L, cur_R, 7-cur, cur 
        r -= 1
        grid[r][c] = cur
    else:
        if r+1 >= n:
            continue
        cur, cur_L, cur_R, cur_U, cur_D = cur_D, cur_L, cur_R, cur, 7-cur 
        r += 1
        grid[r][c] = cur

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]
print(ans)