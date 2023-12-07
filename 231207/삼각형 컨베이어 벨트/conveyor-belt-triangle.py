n, t = tuple(map(int, input().split()))
arr = []
for _ in range(3):
    arr += list(map(int, input().split()))

cnt = 0
for i in range(3*n - (t%(3*n)), 3*n):
    cnt += 1
    print(arr[i], end = ' ')
    if cnt % n == 0:
        print()
for i in range(3*n - (t%(3*n))):
    cnt += 1
    print(arr[i], end = ' ')
    if cnt % n == 0:
        print()