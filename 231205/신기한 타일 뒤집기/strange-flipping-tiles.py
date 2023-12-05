n = int(input())
arr = [0] * 200000
cur = 100000
for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(cur, cur - x, -1):
            arr[i] = -1
        cur -= (x - 1)
    else:
        for i in range(cur, cur + x, 1):
            arr[i] = 1
        cur += (x - 1)
cnt_white = cnt_black = 0
for elem in arr:
    if elem == -1:
        cnt_white += 1
    if elem == 1:
        cnt_black += 1
print(cnt_white, cnt_black)