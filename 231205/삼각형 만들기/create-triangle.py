N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

max_val = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] != arr[j][0]:
            continue
        for k in range(N):
            if k == i or k == j:
                continue 
            if arr[i][1] != arr[k][1]:
                continue
            max_val = max(max_val, abs(arr[i][1] - arr[j][1]) * abs(arr[i][0] - arr[k][0]))
print(max_val)