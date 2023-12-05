def f(n):
    N = str(n)
    for i in range(len(N)//2):
        if N[i] != N[len(N) - 1 - i]:
            return False
    return True

X, Y = tuple(map(int, input().split()))
cnt = 0
for i in range(X, Y+1):
    if f(i):
        cnt += 1
print(cnt)