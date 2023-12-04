arr = input().split()
h, w = int(arr[0]), int(arr[1])
h /= 100
bmi = int(w / h / h)
print(bmi)
if bmi >= 25:
    print("Obesity")