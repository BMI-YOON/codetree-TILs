arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr_2d[i][j]
    print(f"{sum / 4:.1f}", end = ' ')
print()

for j in range(4):
    sum = 0
    for i in range(2):
        sum += arr_2d[i][j]
    print(f"{sum / 2:.1f}", end = ' ')
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum += arr_2d[i][j]
print(f"{sum / 8:.1f}")