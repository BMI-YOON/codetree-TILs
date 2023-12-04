a, b = tuple(map(int, input().split()))
count_arr = [0] * 10
while a > 1:
    count_arr[a % b] += 1
    a, b = a // b, b
sum = 0
for elem in count_arr:
    sum += elem ** 2
print(sum)