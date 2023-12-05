n, t = tuple(map(int, input().split()))
r, c, d = input().split()
r, c = int(r), int(c)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]
mapper = {
    'U': 2,
    'D': 1,
    'R': 0,
    'L': 3
}
x, y = c - 1, r - 1
cur_dir = mapper[d]
for _ in range(t):
    if not in_range(x + dxs[cur_dir], y + dys[cur_dir]):
        cur_dir = 3 - cur_dir 
    else:
        x, y = x + dxs[cur_dir], y + dys[cur_dir]
print(y + 1, x + 1)