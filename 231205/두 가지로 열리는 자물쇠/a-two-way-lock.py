N = int(input())
a1, b1, c1 = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))

def f(a, b):
    if a > b:
        a, b = b, a 
    if b - a <= 2:
        return True
    if b == (N-1) and a == 1:
        return True 
    if b == N and a == 1:
        return True 
    if b == N and a == 2:
        return True 
    return False 

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if (f(i, a1) and f(j, b1) and f(k, c1)) or (f(i, a2) and f(j, b2) and f(k, c2)):
                cnt += 1
print(cnt)