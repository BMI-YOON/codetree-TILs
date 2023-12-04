arr = input().split()
m, f = int(arr[0]), int(arr[1])
if m < 90:
    print(0)
elif f >= 95:
    print(100000)
elif f >= 90:
    print(50000)
else:
    print(0)