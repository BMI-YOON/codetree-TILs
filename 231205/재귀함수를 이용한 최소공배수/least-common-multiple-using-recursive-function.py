def lcm(a, b):
    max_val = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_val = i 
    return a * b // max_val

def f(n):
    if n == 1:
        return arr[0]
    return lcm(f(n-1), arr[n-1])

n = int(input())
arr = list(map(int, input().split()))
print(f(n))