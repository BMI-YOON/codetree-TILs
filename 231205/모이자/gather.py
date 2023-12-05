import sys

n = int(input())
arr = list(map(int, input().split()))

min_num = sys.maxsize
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j] * abs(j - i)
    min_num = min(min_num, sum)
print(min_num)