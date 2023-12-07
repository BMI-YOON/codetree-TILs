T = int(input())
dir_mapper = {'U':0, 'R':1, 'L':2, 'D':3}
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
EMPTY = (-1, -1)

def in_range(x, y):
    if 0 <= x and x <= 4000 and 0 <= y and y <= 4000:
        return True
    return False

grid = [
    [-1 for _ in range(4001)]
    for _ in range(4001)
]

for _ in range(T):
    marvles = []
    N = int(input())
    for i in range(N):
        x, y, w, d = input().split()
        marvles.append((2*int(x)+2000, 2*int(y)+2000, int(w), i+1, dir_mapper[d]))
    ans = -1
    for t in range(1, 4001):
        next_marvles_idx = []
        for idx in range(len(marvles)):
            ni, nj = marvles[idx][0] + dxs[marvles[idx][4]], marvles[idx][1] + dys[marvles[idx][4]]
            if not in_range(ni, nj):
                continue 
            if grid[ni][nj] != -1:
                ans = t
                if marvles[grid[ni][nj]][2] < marvles[idx][2] or (marvles[grid[ni][nj]][2] == marvles[idx][2] and marvles[grid[ni][nj]][3] < marvles[idx][3]):
                    grid[ni][nj] = idx
            else:
                grid[ni][nj] = idx
                next_marvles_idx.append((ni, nj))
        next_marvles = []
        for i, j in next_marvles_idx:
            next_marvles.append((i, j, marvles[grid[i][j]][2], marvles[grid[i][j]][3], marvles[grid[i][j]][4]))
            grid[i][j] = -1
        marvles = next_marvles
    print(ans)