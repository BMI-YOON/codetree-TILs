n = int(input())
cnt = 65
for _ in range(n):
    for _ in range(n):
        print(chr(cnt), end = '')
        cnt += 1
    print()