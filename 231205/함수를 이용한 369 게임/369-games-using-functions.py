def f(n):
    if n % 3 == 0:
        return True
    else:
        while True:
            if n % 10 == 3 or n % 10 == 6 or n% 10 == 9:
                return True 
            else:
                n = n // 10
                if n == 0:
                    return False

a, b = tuple(map(int, input().split()))
cnt = 0
for i in range(a, b+1):
    if f(i):
        cnt += 1
print(cnt)