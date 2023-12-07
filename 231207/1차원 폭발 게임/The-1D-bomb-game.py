N, M = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(N)
]

while True:
    if not arr:
        print(0)
        break

    cur_num, cur_cnt, start_idx, flag = arr[0], 0, 0, 0
    for i in range(len(arr)):
        if arr[i] == cur_num:
            cur_cnt += 1
            if cur_cnt == M:
                flag = 1
                for j in range(start_idx, i+1):
                    arr[j] = 0
            elif cur_cnt > M:
                arr[i] = 0
        else:
            cur_num, cur_cnt, start_idx = arr[i], 1, i
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
    arr = temp.copy()
    if flag == 0:
        print(len(arr))
        for elem in arr:
            print(elem)
        break