N = int(input())
arr = list(input())
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] == 'C' and arr[j] == 'O' and arr[k] == 'W':
                cnt += 1
print(cnt)