n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
for _ in range(q):
    question = input().split()
    num = int(question[0])
    if num < 3:
        a = int(question[1])
    else:
        a, b = int(question[1]), int(question[2])

    if num == 1:
        print(arr[a - 1])
    elif num == 2:
        if a in arr:
            print(arr.index(a) + 1)
        else:
            print(0)
    else:
        for i in range(a - 1, b):
            print(arr[i], end = ' ')
        print()