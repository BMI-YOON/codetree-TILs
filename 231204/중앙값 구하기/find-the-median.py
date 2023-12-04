arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
if a < b < c:
    print(b)
elif a < c < b:
    print(c)
elif b < a < c:
    print(a)
elif b < c < a:
    print(c)
elif c < a < b:
    print(a)
else:
    print(b)