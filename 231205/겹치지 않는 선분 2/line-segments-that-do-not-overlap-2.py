N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

cnt = 0
for i in range(N):
    boolean = False
    for j in range(N):
        if j == i:
            continue
        if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
            boolean = True
        if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
            boolean = True
    if not boolean:
        cnt += 1
print(cnt)