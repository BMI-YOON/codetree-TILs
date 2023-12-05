def f(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum // 10

N = int(input())
print(f(N))