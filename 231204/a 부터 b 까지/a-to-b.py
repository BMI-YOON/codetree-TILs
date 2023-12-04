arr = input().split()
a, b = int(arr[0]), int(arr[1])
cur = a
while cur <= b:
    print(cur, end = ' ')
    if cur % 2 == 1:
        cur *= 2
    else:
        cur += 3