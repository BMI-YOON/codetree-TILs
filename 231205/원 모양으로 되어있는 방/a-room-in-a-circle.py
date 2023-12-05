import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

min_num = sys.maxsize
for i in range(N):
    sum = 0
    for j in range(i+1, N):
        sum += arr[j] * (j - i)
    for j in range(0, i):
        sum += arr[j] * (N - (i - j))
    min_num = min(min_num, sum)
print(min_num)