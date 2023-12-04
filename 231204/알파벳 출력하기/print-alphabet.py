n = int(input())
cnt = 65
for i in range(n):
    for _ in range(i+1):
        print(chr(cnt), end = '')
        cnt += 1
        if cnt == 65 + 26:
            cnt = 65
    print()