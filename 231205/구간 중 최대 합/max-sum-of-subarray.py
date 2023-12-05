n , k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
max_val = 0
for i in range(0, n-k+1):
    sum = 0
    for j in range(k):
        sum += arr[i+j]
    max_val = max(max_val, sum)
print(max_val)