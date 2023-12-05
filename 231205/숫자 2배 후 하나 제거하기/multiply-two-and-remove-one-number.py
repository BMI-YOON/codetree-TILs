import sys
n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize
for k in range(n):
    arr[k] *= 2
    for i in range(n):
        sum = 0
        new_arr = [value for index, value in enumerate(arr) if index != i]
        for j in range(len(new_arr) - 1):
            sum += abs(new_arr[j+1] - new_arr[j])
        ans = min(ans, sum)
    arr[k] //= 2
print(ans)