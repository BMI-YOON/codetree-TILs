import sys

N, S = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
sum = sum(arr)
min_num = sys.maxsize

for i in range(N):
    for j in range(i+1, N):
        min_num = min(min_num, abs(sum - arr[i] - arr[j] - S))
print(min_num)