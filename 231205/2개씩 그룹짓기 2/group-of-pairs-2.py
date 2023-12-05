import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_val = sys.maxsize
for i in range(n):
    min_val = min(min_val, arr[i+n] - arr[i])
print(min_val)