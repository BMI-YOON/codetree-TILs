n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    cnt += A[i] - B[i]
    A[i+1] = A[i+1] + A[i] - B[i]
print(cnt)