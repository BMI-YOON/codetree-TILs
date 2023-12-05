N = int(input())
arr = list(map(int, input().split()))
ans_arr = sorted(arr)

cnt = 0
while arr != ans_arr:
    last_idx, idx, num = -1, -1, 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                last_idx = i 
    for i in range(last_idx + 1, N):
        if arr[i] > arr[0]:
            num = arr[0]
            idx = i - 1
            break
        if i == N - 1:
            num = arr[0]
            idx = i
    for i in range(idx):
        arr[i] = arr[i+1]
    arr[idx] = num 
    cnt += 1

print(cnt)