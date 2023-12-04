N = int(input())
arr = list(map(int, input().split()))
max_idx = N
while True:
    if max_idx == 0:
        break
    max_val = 0
    for i in range(0, max_idx):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    print(max_idx + 1, end = ' ')