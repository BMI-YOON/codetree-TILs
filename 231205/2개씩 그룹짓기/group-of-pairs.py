N = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_val = 0
for i in range(N):
    if arr[i] + arr[2 * N - i - 1] > max_val:
        max_val = arr[i] + arr[2 * N - i - 1]
print(max_val)