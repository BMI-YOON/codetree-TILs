arr = list(map(int, input().split()))
arr_1 = arr[::2]
arr_2 = arr[1::2]
if sum(arr_1) > sum(arr_2):
    print(sum(arr_1) - sum(arr_2))
else:
    print(sum(arr_2) - sum(arr_1))