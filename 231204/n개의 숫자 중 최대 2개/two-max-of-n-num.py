N = int(input())
arr = list(map(int, input().split()))
if arr[0] > arr[1]:
    max_val_1, max_val_2 = arr[0], arr[1]
elif arr[0] == arr[1]:
    max_val_1 = max_val_2 = arr[0]
else:
    max_val_1, max_val_2 = arr[1], arr[0]
for elem in arr[2:]:
    if elem > max_val_1:
        max_val_1, max_val_2 = elem, max_val_1 
    elif elem == max_val_1:
        max_val_2 = max_val_1
    elif max_val_1 > elem > max_val_2:
        max_val_2 = elem 
print(max_val_1, max_val_2)