sq = input().split()
s = sq[0]
q = int(sq[1])
for _ in range(q):
    question = input().split()
    num = int(question[0])
    if num == 1:
        a, b = int(question[1]), int(question[2])
        arr = list(s)
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
        s = ''.join(arr)
        print(s)
    else:
        a, b = question[1], question[2]
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == a:
                arr[i] = b
        s = ''.join(arr)
        print(s)