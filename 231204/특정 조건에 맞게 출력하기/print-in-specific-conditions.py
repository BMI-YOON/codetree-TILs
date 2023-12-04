arr = list(map(int, input().split()))
for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 1:
        print(elem + 3, end = ' ')
    else:
        print(elem // 2, end = ' ')