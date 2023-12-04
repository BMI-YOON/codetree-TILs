n, A = input().split()
n = int(n)
cnt = 0
for _ in range(n):
    if A == input():
        cnt += 1
print(cnt)