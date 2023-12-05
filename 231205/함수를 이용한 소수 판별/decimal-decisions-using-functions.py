def f(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 1: 
        return False
    return True

sum = 0
a, b = tuple(map(int, input().split()))
for i in range(a, b+1):
    if f(i):
        sum += i 
print(sum)