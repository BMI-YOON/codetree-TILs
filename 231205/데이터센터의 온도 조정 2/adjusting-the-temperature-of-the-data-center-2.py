import sys
N, C, G, H = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
min_T, max_T = sys.maxsize, -sys.maxsize 

for elem in arr:
    min_T = min(min_T, elem[0])
    max_T = max(max_T, elem[1])

ans = -sys.maxsize
for T in range(min_T-1, max_T+2):
    sum = 0
    for elem in arr:
        if T < elem[0]:
            sum += C
        elif elem[0] <= T and T <= elem[1]:
            sum += G
        else:
            sum += H
    ans = max(ans, sum)
print(ans)