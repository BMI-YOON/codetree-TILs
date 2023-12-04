arr = input().split()
a, b = int(arr[0]), int(arr[1])
if a > b:
    a, b = b, a
sum = 0
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i 
print(sum)