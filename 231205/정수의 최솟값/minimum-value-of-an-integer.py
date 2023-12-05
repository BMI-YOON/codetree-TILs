def f(*args):
    return min(args)

a, b, c = tuple(map(int, input().split()))
print(f(a, b, c))