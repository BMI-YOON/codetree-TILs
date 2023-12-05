import sys

N, H, T = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(0, N-T+1):
    sum = 0
    for j in range(i, i+T):
        sum += abs(arr[j] - H)
    min_val = min(min_val, sum)
print(min_val)