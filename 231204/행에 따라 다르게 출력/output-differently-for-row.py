n = int(input())
cnt = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j != n-1:
            print(cnt, end = ' ')
            cnt += 1
        elif i % 2 == 1 and j == n-1:
            print(cnt, end = ' ')
            cnt += 1
        else:
            print(cnt, end = ' ')
            cnt += 2
    print()