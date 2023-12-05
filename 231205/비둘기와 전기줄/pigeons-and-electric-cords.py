N = int(input())
arr = [-1] * 11
cnt = 0
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    if arr[a] != -1 and arr[a] != b:
        cnt += 1
    arr[a] = b
print(cnt)