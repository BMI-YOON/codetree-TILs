cnt = 0
sum = 0
for _ in range(10):
    num = int(input())
    if 0 <= num <= 200:
        cnt += 1
        sum += num 
print(sum, f"{sum/cnt:.1f}")