a, b = tuple(map(int, input().split()))
cnt = 0
for elem in str(a+b):
    if elem == '1':
        cnt += 1
print(cnt)