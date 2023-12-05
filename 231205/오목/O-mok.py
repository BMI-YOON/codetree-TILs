arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

ans, x, y = 0, -1, -1
for i in range(15):
    for j in range(19):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] == 1 and arr[i+3][j] == 1 and arr[i+4][j] == 1:
            ans = 1
            x, y = i+2, j
        if arr[i][j] == 2 and arr[i+1][j] == 2 and arr[i+2][j] == 2 and arr[i+3][j] == 2 and arr[i+4][j] == 2:
            ans = 2
            x, y = i+2, j

for i in range(19):
    for j in range(15):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1 and arr[i][j+3] == 1 and arr[i][j+4] == 1:
            ans = 1
            x, y = i, j+2
        if arr[i][j] == 2 and arr[i][j+1] == 2 and arr[i][j+2] == 2 and arr[i][j+3] == 2 and arr[i][j+4] == 2:
            ans = 2
            x, y = i, j+2

for i in range(15):
    for j in range(15):
        if arr[i][j] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+3][j+3] == 1 and arr[i+4][j+4] == 1:
            ans = 1
            x, y = i+2, j+2
        if arr[i+4][j] == 1 and arr[i+3][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+1][j+3] == 1 and arr[i][j+4] == 1:
            ans = 1
            x, y = i+2, j+2
        if arr[i][j] == 2 and arr[i+1][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+3][j+3] == 2 and arr[i+4][j+4] == 2:
            ans = 2
            x, y = i+2, j+2
        if arr[i+4][j] == 2 and arr[i+3][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+1][j+3] == 2 and arr[i][j+4] == 2:
            ans = 2
            x, y = i+2, j+2

print(ans)
if ans != 0:
    print(x + 1, y + 1)