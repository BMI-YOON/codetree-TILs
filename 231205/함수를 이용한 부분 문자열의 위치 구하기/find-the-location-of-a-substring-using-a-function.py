def f(A, B):
    for i in range(len(A) - len(B) + 1):
        if A[i:len(B)+i] == B:
            return i 
    return -1

A = input()
B = input()
print(f(A, B))