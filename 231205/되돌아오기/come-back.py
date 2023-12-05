N = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
mapper = {
    'W': 2,
    'S': 1,
    'N': 3,
    'E': 0
}
x, y, t, ans = 0, 0, 0, -1
for _ in range(N):
    dir_char, dist = input().split()
    dist = int(dist)
    for _ in range(dist):
        x, y = x + dxs[mapper[dir_char]], y + dys[mapper[dir_char]]
        t += 1
        if x == 0 and y == 0:
            ans = t
            break
    if x == 0 and y == 0:
        break
print(ans)