arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(2, 10, 2):
    for j in range(b, a - 1, -1):
        print(f"{j} * {i} = {i * j}", end = ' ')
        if j != a:
            print('/', end = ' ')
    print()