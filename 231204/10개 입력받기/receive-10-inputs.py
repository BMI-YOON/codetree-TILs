arr = list(map(int, input().split()))
sum = 0
len = 0
for elem in arr:
    if elem != 0:
        sum += elem
        len += 1
    else:
        break
print(sum, f"{sum/len:.1f}")