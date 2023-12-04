n = int(input())
for _ in range(n):
    prod = 1
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    for i in range(a, b+1):
        prod *= i 
    print(prod)