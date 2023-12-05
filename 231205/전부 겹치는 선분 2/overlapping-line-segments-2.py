n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

for i in range(n):
    max_x1, min_x2 = 0, 101
    for j in range(n):
        if j == i:
            continue
        max_x1 = max(max_x1, arr[j][0])
        min_x2 = min(min_x2, arr[j][1])
    if max_x1 <= min_x2:
        print("Yes")
        break
    if i == n-1:
        print("No")
        break