N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_val = 0
for i in range(N-2):
    for j in range(N-2):
        max_val = max(max_val, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
print(max_val)