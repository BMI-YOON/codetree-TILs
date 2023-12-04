A = input()
B = input()
arr = list(A)
while True:
    if B in A:
        arr = list(A)
        index = A.find(B)
        for _ in range(len(B)):
            arr.pop(index)
        A = ''.join(arr)
    else:
        break
A = ''.join(arr)
print(A)