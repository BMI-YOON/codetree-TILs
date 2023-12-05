def f(n):
    if n == 1:
        return arr[0]
    cur_max = f(n-1)
    if cur_max >= arr[n-1]:
        return cur_max
    else:
        return arr[n-1]

n = int(input())
arr = list(map(int, input().split()))
print(f(n))