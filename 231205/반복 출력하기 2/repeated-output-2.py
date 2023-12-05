def f(N):
    if N == 0:
        return
    f(N-1)
    print("HelloWorld")

N = int(input())
f(N)