n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def f(num):
    if num < max(arr):
        return False
    sum, cnt = 0, 0
    for i in range(n):
        if sum + arr[i] <= num:
            sum += arr[i]
        else:
            sum = arr[i]
            cnt += 1
    if cnt <= m - 1:
        return True
    else:
        return False 

for i in range(1, 10001):
    if f(i):
        print(i)
        break