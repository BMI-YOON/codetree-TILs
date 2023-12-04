arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(1, 10):
    for j in range((b - a) // 2 + 1):
        print(f"{b - 2 * j} * {i} = {(b - 2 * j) * (i)}", end = ' ')
        if j != (b - a) // 2:
            print('/', end = ' ')
    print()