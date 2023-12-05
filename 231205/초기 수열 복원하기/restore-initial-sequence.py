N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N+1):
    cnt_arr = [0] * (2000+1)
    cur = i
    ans_arr = [cur]
    for j in range(N-1):
        if arr[j] - cur <= 0:
            break
        cur = arr[j] - cur 
        cnt_arr[cur] += 1
        if cnt_arr[cur] >= 2:
            break
        ans_arr.append(cur)
    if len(ans_arr) == N:
        for elem in ans_arr:
            print(elem, end = ' ')
        break