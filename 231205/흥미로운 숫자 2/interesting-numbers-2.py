def f(n):
    cnt = [0] * 10
    while n > 0:
        cnt[n % 10] += 1
        n //= 10
    cnt.sort()
    return cnt[0] + cnt[1] + cnt[2] + cnt[3] + cnt[4] + cnt[5] + cnt [6] + cnt[7] == 0 and cnt[8] == 1

X, Y = tuple(map(int, input().split()))
cnt = 0
for i in range(X, Y+1):
    if f(i):
        cnt += 1
print(cnt)