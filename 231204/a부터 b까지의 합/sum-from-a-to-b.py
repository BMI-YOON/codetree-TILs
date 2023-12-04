arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum = 0
for i in range(a, b+1):
    sum += i
print(sum)