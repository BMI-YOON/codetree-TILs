N, B = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort() 

ans = 0
for i in range(N):
    sum = 0
    for j in range(i):
        sum += arr[j]
    sum += arr[i] // 2
    if sum <= B:
        ans = i + 1
print(ans)