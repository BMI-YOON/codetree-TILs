N = int(input())
arr = [0] * 101
for _ in range(N):
    a, b = input().split()
    arr[int(a)] = b

for ans in range(100, -1, -1):
    flag = 0
    for i in range(0, 100-ans+1):
        if arr[i] == 0 or arr[i+ans] == 0:
            continue
        cnt_G, cnt_H = 0, 0
        for j in range(i, i+ans+1):
            if arr[j] == 'G':
                cnt_G += 1
            if arr[j] == 'H':
                cnt_H += 1
        if cnt_G == ans + 1:
            print(ans)
            flag = 1
            break
        if cnt_H == ans + 1:
            print(ans)
            flag = 1
            break 
        if cnt_G == cnt_H:
            print(ans)
            flag = 1
            break 
    if flag == 1:
        break