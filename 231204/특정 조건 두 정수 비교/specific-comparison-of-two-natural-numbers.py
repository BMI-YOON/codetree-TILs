arr = input().split()
a, b = int(arr[0]), int(arr[1])
if a < b:
    print(1, end = ' ')
else:
    print(0, end = ' ')
if a == b:
    print(1)
else:
    print(0)