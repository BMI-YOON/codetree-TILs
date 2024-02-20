n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
dir = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())
r, c = r-1, c-1

ans = 0

dxs, dys = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    global n, num, dir, ans

    return 0 <= x and x < n and 0 <= y and y < n

def candidate(x, y):
    global n, num, dir, ans

    arr = list()
    cur_num = num[x][y]
    cur_dir = dir[x][y]
    while True:
        next_x = x + dxs[cur_dir]
        next_y = y + dys[cur_dir]
        if not in_range(next_x, next_y):
            break
        else:
            if num[next_x][next_y] > cur_num:
                arr.append((next_x, next_y))
            x, y = next_x, next_y
    return arr

def simulate(cur_r, cur_c, cnt):
    global n, num, dir, ans 
    
    arr = candidate(cur_r, cur_c)
    if len(arr) == 0:
        ans = max(ans, cnt)
        return 
    else:
        for x, y in arr:
            simulate(x, y, cnt+1)

simulate(r, c, 0)
print(ans)