A = input()
B = input()
for i in range(len(A)):
    A = A[-1] + A[0:-1]
    if A == B:
        print(i + 1)
        break
    if i == len(A) - 1:
        print(-1)