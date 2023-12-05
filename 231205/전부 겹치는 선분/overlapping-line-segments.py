n = int(input())
cnt = [0] * 101
for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    for j in range(x1, x2+1):
        cnt[j] += 1
flag = 0
for elem in cnt:
    if elem == n:
        print("Yes")
        flag = 1
        break
if flag == 0:
    print("No")