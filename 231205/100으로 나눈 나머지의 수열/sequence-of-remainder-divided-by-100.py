def f(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    return f(N-1) * f(N-2) % 100

N = int(input())
print(f(N))