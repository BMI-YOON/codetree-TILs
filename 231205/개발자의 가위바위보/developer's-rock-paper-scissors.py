N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

case1, case2 = 0, 0
for i in range(N):
    if arr[i][0] == 1 and arr[i][1] == 2:
        case1 += 1
    elif arr[i][0] == 1 and arr[i][1] == 3:
        case2 += 1
    elif arr[i][0] == 2 and arr[i][1] == 1:
        case2 += 1
    elif arr[i][0] == 2 and arr[i][1] == 3:
        case1 += 1
    elif arr[i][0] == 3 and arr[i][1] == 1:
        case1 += 1
    elif arr[i][0] == 3 and arr[i][1] == 2:
        case2 += 1
print(max(case1, case2))