def function(n, m):
    max_val = 1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            max_val = i 
    print(max_val)

n, m = tuple(map(int, input().split()))
function(n, m)