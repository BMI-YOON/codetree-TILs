def f(N):
    if N < 10:
        return N ** 2
    return f(N // 10) + (N % 10) ** 2

N = int(input())
print(f(N))