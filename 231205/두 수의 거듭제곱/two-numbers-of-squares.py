def f(a, b):
    num = 1
    for _ in range(b):
        num *= a
    return num 

a, b = tuple(map(int, input().split()))
print(f(a, b))