n = int(input())
arr = list(map(int, input().split()))
min_val = arr[1] - arr[0]
for i in range(0, n-1):
    if arr[i+1] - arr[i] < min_val:
        min_val = arr[i+1] - arr[i]
print(min_val)