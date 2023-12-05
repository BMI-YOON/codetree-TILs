N = int(input())
cnt = 1
last = int(input())
max_cnt = 1
for _ in range(N-1):
    cur = int(input())
    if cur == last:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 1
    last = cur
print(max_cnt)