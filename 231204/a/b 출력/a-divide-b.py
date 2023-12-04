arr = input().split()
a, b = int(arr[0]), int(arr[1])
print(a // b, end = '')
print('.', end = '')
r = a % b
for _ in range(20):
    print(r * 10 // b, end = '')
    r = r * 10 % b