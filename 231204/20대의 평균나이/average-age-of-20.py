sum = cnt = 0
while True:
    age = int(input())
    if age < 20 or age >= 30: 
        break
    sum += age 
    cnt += 1
print(f"{sum/cnt:.2f}")