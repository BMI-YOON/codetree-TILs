arr = [
    list(input())
    for _ in range(10)
]

Bx, By, Lx, Ly, Rx, Ry = -1, -1, -1, -1, -1, -1
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            Bx, By = i, j
        if arr[i][j] == 'L':
            Lx, Ly = i, j
        if arr[i][j] == 'R':
            Rx, Ry = i, j

if Lx == Rx and Rx == Bx and (Ly < Ry < By or Ly > Ry > By):
    print(abs(Lx - Bx) + abs(Ly - By) - 1 + 2)
elif Ly == Ry and Ry == By and (Lx < Rx < Bx or Lx > Rx > Bx):
    print(abs(Lx - Bx) + abs(Ly - By) - 1 + 2)
else:
    print(abs(Lx - Bx) + abs(Ly - By) - 1)