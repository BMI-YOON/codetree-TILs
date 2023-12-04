arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum = 0
num = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i 
        num += 1
print(sum, f"{sum/num:.1f}")