n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = 0
for i in range(n-1):
    for j in range(m-1):
        max_val = max(max_val, arr[i][j] + arr[i+1][j] + arr[i][j+1])
        max_val = max(max_val, arr[i][j] + arr[i+1][j] + arr[i+1][j+1])
        max_val = max(max_val, arr[i][j] + arr[i][j+1] + arr[i+1][j+1])
        max_val = max(max_val, arr[i+1][j+1] + arr[i+1][j] + arr[i][j+1])

for i in range(n):
    for j in range(m-2):
        max_val = max(max_val, arr[i][j] + arr[i][j+1] + arr[i][j+2])

for i in range(n-2):
    for j in range(m):
        max_val = max(max_val, arr[i][j] + arr[i+1][j] + arr[i+2][j])

print(max_val)