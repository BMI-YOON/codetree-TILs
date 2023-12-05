import sys
arr = list(map(int, input().split()))
sum = sum(arr)
min_val = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_val = min(min_val, abs(2 * (arr[i] + arr[j] + arr[k]) - sum))
print(min_val)