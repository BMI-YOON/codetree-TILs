def f(N):
    if N == 0:
        return
    print(N, end = ' ')
    f(N-1)
    print(N, end = ' ')

N = int(input())
f(N)