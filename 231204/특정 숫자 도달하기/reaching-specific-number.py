arr = list(map(int, input().split()))
sum = 0
cnt = 0
for elem in arr:
    if elem < 250:
        sum += elem
        cnt += 1
    else:
        break
print(sum, f"{sum/cnt:.1f}")