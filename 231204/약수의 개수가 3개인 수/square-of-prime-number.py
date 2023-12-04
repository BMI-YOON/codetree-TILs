arr = input().split()
a, b = int(arr[0]), int(arr[1])
cnt = 0
for i in range(a, b+1):
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 3:
        cnt += 1
print(cnt)