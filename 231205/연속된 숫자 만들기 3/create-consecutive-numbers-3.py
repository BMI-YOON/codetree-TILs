arr = list(map(int, input().split()))
arr.sort()
cnt = 0
while True:
    if arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1:
        print(cnt)
        break
    if arr[1] - arr[0] > arr[2] - arr[1]:
        arr[2] = arr[1] - 1
        arr[1], arr[2] = arr[2], arr[1]
    else:
        arr[0] = arr[1] + 1
        arr[0], arr[1] = arr[1], arr[0]
    cnt += 1