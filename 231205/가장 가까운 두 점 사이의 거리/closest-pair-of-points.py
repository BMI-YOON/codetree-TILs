import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

min_val = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        min_val = min(min_val, (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
print(min_val)