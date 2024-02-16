N, M, C = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

def value(x, y, cnt, weight, val):
    global N, M, C, grid, ans_val
    if cnt == M:
        if weight <= C:
            ans_val = max(ans_val, val)
        return
    
    value(x, y, cnt+1, weight, val)
    
    weight += grid[x][y+cnt]
    val += grid[x][y+cnt] ** 2
    value(x, y, cnt+1, weight, val)
    #weight -= grid[x][y+cnt]
    #val -= grid[x][y+cnt] ** 2

def in_range(x, y):
    global N
    return 0 <= x and x < N and 0 <= y and y < N

output = 0
for x1 in range(N):
    for y1 in range(N):
        for x2 in range(x1, N):
            for y2 in range(N):
                if y1+M-1 >= N or y2+M-1 >= N:
                    continue 
                if x1 == x2 and not (y1+M-1 < y2 or y2+M-1 < y1):
                    continue
                ans = 0
                ans_val = 0
                value(x1, y1, 0, 0, 0)
                ans += ans_val
                ans_val = 0
                value(x2, y2, 0, 0, 0)
                ans += ans_val
                output = max(output, ans)

print(output)