def include(x, y, a, b):
    if x == -1:
        return b == y
    if y == -1:
        return a == x

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

ans = 0
for i in range(11):
    for j in range(11):
        for k in range(11):
            flag1, flag2, flag3, flag4 = 0, 0, 0, 0
            for l in range(N):
                if include(i, -1, arr[l][0], arr[l][1]) or include(j, -1, arr[l][0], arr[l][1]) or include(k, -1, arr[l][0], arr[l][1]):
                    flag1 += 1
                if include(i, -1, arr[l][0], arr[l][1]) or include(j, -1, arr[l][0], arr[l][1]) or include(-1, k, arr[l][0], arr[l][1]):
                    flag2 += 1
                if include(i, -1, arr[l][0], arr[l][1]) or include(-1, j, arr[l][0], arr[l][1]) or include(-1, k, arr[l][0], arr[l][1]):
                    flag3 += 1
                if include(-1, i, arr[l][0], arr[l][1]) or include(-1, j, arr[l][0], arr[l][1]) or include(-1, k, arr[l][0], arr[l][1]):
                    flag4 += 1
            if flag1 == N or flag2 == N or flag3 == N or flag4 == N:
                ans = 1
print(ans)