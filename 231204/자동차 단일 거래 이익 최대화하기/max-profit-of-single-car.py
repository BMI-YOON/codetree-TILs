n = int(input())
arr = list(map(int, input().split()))
max_val = 0
cur_min = arr[0]
for elem in arr:
    if max_val < (elem - cur_min):
        max_val = elem - cur_min
    if elem < cur_min:
        cur_min = elem
print(max_val)