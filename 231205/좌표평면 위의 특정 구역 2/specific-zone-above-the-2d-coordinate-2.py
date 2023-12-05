import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

min_val = sys.maxsize
for i in range(N):
    min_x, max_x, min_y, max_y = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize
    for j in range(N):
        if j == i:
            continue
        min_x = min(min_x, arr[j][0])
        max_x = max(max_x, arr[j][0])
        min_y = min(min_y, arr[j][1])
        max_y = max(max_y, arr[j][1])
    min_val = min(min_val, (max_x - min_x) * (max_y - min_y))
print(min_val)