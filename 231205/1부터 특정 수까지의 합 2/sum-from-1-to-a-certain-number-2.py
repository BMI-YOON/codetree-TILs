def f(N):
    if N == 1:
        return 1
    return f(N-1) + N

N = int(input())
print(f(N))