m1, d1, m2, d2 = tuple(map(int, input().split()))
sum1 = sum2 = 0
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, m1):
    sum1 += days[i]
sum1 += d1 
for i in range(1, m2):
    sum2 += days[i]
sum2 += d2 
string = input()
if string == 'Mon':
    num = 0
elif string == 'Tue':
    num = 1
elif string == 'Wed':
    num = 2
elif string == 'Thu':
    num = 3
elif string == 'Fri':
    num = 4
elif string == 'Sat':
    num = 5
else:
    num = 6

print((sum2 - sum1) // 7 + (1 if (sum2 - sum1) % 7 >= num else 0))