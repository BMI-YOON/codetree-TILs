n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))
for _ in range(m):
    a1, a2 = tuple(map(int, input().split()))
    sum = 0
    for i in range(a1 - 1, a2):
        sum += A[i]
    print(sum)