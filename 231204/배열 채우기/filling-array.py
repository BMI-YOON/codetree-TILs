arr = list(map(int, input().split()))
len = 0
for elem in arr:
    if elem != 0:
        len += 1
    else:
        break
for elem in arr[len-1::-1]:
    print(elem, end = ' ')