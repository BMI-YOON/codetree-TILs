n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def cal(i, j, x, y):
    sum = arr[i][j]
    for k in range(1, x+1):
        sum += arr[i-k][j+k]
    for k in range(1, y+1):
        sum += arr[i-x-k][j+x-k]
    for k in range(1, x+1):
        sum += arr[i-x-y+k][j+x-y-k]
    for k in range(1, y):
        sum += arr[i-y+k][j-y+k]
    return sum

def f(a, b):
    if a < 0 or a >= n:
        return False
    if b < 0 or b >= n:
        return False 
    return True

max_val = 0
for i in range(n):
    for j in range(n):
        for x in range(1, n):
            for y in range(1, n):
                if not f(i-x, j+x):
                    continue
                if not f(i-x-y, j+x-y):
                    continue 
                if not f(i-y, j-y):
                    continue 
                max_val = max(max_val, cal(i, j, x, y))
print(max_val)