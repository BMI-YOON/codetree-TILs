arr = input().split()
a, n = int(arr[0]), int(arr[1])
cur = a
for _ in range(n):
    print(cur + n)
    cur += n