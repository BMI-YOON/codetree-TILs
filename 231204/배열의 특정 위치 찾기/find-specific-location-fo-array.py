arr = list(map(int, input().split()))
arr_2 = arr[1::2]
arr_3 = arr[2::3]
print(sum(arr_2), f"{sum(arr_3)/len(arr_3):.1f}")