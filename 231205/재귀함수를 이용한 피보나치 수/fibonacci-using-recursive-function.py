def f(N):
    if N == 1 or N == 2:
        return 1
    return f(N-2) + f(N-1)

N = int(input())
print(f(N))