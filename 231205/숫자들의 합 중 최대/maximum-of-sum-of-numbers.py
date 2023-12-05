def f(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

X, Y = tuple(map(int, input().split()))
max_val = 0
for i in range(X, Y+1):
    max_val = max(max_val, f(i))
print(max_val)