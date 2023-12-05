def f1(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def f2(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    if sum % 2 == 0:
        return True
    else:
        return False

a, b = tuple(map(int, input().split()))
cnt = 0
for i in range(a, b+1):
    if f1(i) and f2(i):
        cnt += 1
print(cnt)