m1, d1, m2, d2 = tuple(map(int, input().split()))
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum1 = sum2 = 0
for i in range(1, m1):
    sum1 += days[i]
sum1 += d1 
for i in range(1, m2):
    sum2 += days[i]
sum2 += d2 
if (sum2 - sum1) % 7 == 0:
    print("Mon")
elif (sum2 - sum1) % 7 == 1:
    print("Tue")
elif (sum2 - sum1) % 7 == 2:
    print("Wed")
elif (sum2 - sum1) % 7 == 3:
    print("Thu")
elif (sum2 - sum1) % 7 == 4:
    print("Fri")
elif (sum2 - sum1) % 7 == 5:
    print("Sat")
else:
    print("Sun")