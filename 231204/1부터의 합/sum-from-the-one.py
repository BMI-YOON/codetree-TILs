n = int(input())
sum = 0
num = 0
for i in range(1, 101):
    if sum >= n:
        break
    sum += i 
    num = i
print(num)