N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_num = 0
for i in range(N):
    for j in range(N-2):
        for k in range(i+1, N):
            for l in range(N-2):
                max_num = max(max_num, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][l] + arr[k][l+1] + arr[k][l+2])
        for m in range(j+3, N-2):
            max_num = max(max_num, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][m] + arr[i][m+1] + arr[i][m+2])
print(max_num)