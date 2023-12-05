n = int(input())
offset = 1000
cur = 0 + 1000
arr = [0] * 2000
for _ in range(n):
    x, RL = input().split()
    x = int(x)
    if RL == 'R':
        for i in range(cur, cur + x):
            arr[i] += 1
        cur += x
    else:
        for i in range(cur - 1, cur - x - 1, -1):
            arr[i] += 1
        cur -= x
cnt = 0
for elem in arr:
    if elem >= 2:
        cnt += 1
print(cnt)