arr = input().split()
a, b = int(arr[0]), int(arr[1])
max = a if a > b else b
print(max)