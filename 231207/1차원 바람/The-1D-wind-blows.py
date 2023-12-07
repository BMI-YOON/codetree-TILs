N, M, Q = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
q = [
    tuple(input().split())
    for _ in range(Q)
]

def shift(r, d):
    if d == 'L':
        tmp = grid[r][M-1]
        for i in range(M-1, 0, -1):
            grid[r][i] = grid[r][i-1]
        grid[r][0] = tmp 
    else:
        tmp = grid[r][0]
        for i in range(0, M-1, 1):
            grid[r][i] = grid[r][i+1]
        grid[r][M-1] = tmp 

def f(a, b):
    for i in range(M):
        if grid[a][i] == grid[b][i]:
            return True
    return False

for elem in q:
    r, d = elem[0], elem[1]
    r = int(r) - 1
    shift(r, d)
    r1, r2 = r, r
    d1, d2 = d, d
    while r1 > 0 and f(r1-1, r1):
        if d1 == 'R':
            d1 = 'L'
        else:
            d1 = 'R'
        r1 -= 1
        shift(r1, d1)
    while r2 < N -1 and f(r2+1, r2):
        if d2 == 'R':
            d2 = 'L'
        else:
            d2 = 'R'
        r2 += 1
        shift(r2, d2)

for i in range(N):
    for j in range(M):
        print(grid[i][j], end = ' ')
    print()