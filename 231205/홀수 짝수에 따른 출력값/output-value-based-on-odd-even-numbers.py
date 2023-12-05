def f(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N % 2 == 1:
        return f(N-2) + N
    else:
        return f(N-2) + N

N = int(input())
print(f(N))