import sys

N = int(input())
grid = [
    list(input())
    for _ in range(N)
]
position = [(-1, -1)] * 11
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'S':
            position[0] = (i, j)
        elif grid[i][j] == 'E':
            position[10] = (i, j)
        elif grid[i][j] != '.':
            position[int(grid[i][j])] = (i, j)

ans = sys.maxsize

def distance(previous, next):
    global position 

    x1, y1 = position[previous]
    x2, y2 = position[next]
    return abs(x1 - x2) + abs(y1 - y2)

def simulate(previous, cur, cnt, cost):
    global N, position, ans 
    
    if cnt == 3:
        cost += distance(previous, 10)
        ans = min(ans, cost)
        return

    if cur == 10:
        return 
    
    simulate(previous, cur+1, cnt, cost)

    if position[cur] != (-1, -1):
        cost += distance(previous, cur)
        simulate(cur, cur+1, cnt+1, cost)

simulate(0, 1, 0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)