import sys

N = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]
min_num = sys.maxsize
for i in range(1, N-1):
    dist = 0
    for j in range(1, i):
        dist += abs(arr_2d[j][0] - arr_2d[j-1][0]) + abs(arr_2d[j][1] - arr_2d[j-1][1])
    dist += abs(arr_2d[i+1][0] - arr_2d[i-1][0]) + abs(arr_2d[i+1][1] - arr_2d[i-1][1])
    for j in range(i+2, N):
        dist += abs(arr_2d[j][0] - arr_2d[j-1][0]) + abs(arr_2d[j][1] - arr_2d[j-1][1])
    min_num = min(min_num, dist)
print(min_num)