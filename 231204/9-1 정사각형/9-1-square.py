n = int(input())
cnt = 9
for _ in range(n):
    for _ in range(n):
        print(cnt, end = '')
        if cnt > 1:
            cnt -= 1
        else:
            cnt = 9
    print()