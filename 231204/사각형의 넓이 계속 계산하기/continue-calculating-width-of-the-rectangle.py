while True:
    arr = input().split()
    row, column, char = int(arr[0]), int(arr[1]), arr[2]
    print(row * column)
    if char == 'C':
        break