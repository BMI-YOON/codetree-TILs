def f(n):
    if n == 0:
        return
    print("* " * n)
    f(n-1)
    print("* " * n)

n = int(input())
f(n)