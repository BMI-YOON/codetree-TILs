arr = list(map(int, input().split()))
sum = 0
len = 0
for elem in arr:
    if elem != 0 and elem % 2 == 0:
        sum += elem  
        len += 1
    elif elem == 0:
        break
print(len, sum)