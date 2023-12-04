arr = input().split()
a, b = int(arr[0]), int(arr[1])
cnt = 0
for i in range(a, b+1):
    num = 0
    for j in range(1, i):
        if i % j == 0:
            num += j
    if num == i:
        cnt += 1
print(cnt)