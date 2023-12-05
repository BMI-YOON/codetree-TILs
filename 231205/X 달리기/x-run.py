X = int(input())
arr = [0]
cur = 1
while True:
    sum = 0
    for i in range(1, cur // 2 + 1):
        sum += i * 2 
    if cur % 2 == 1:
        sum += cur // 2 + 1
    arr.append(sum) 
    cur += 1
    if sum > 100000:
        break

for i in range(len(arr)):
    if arr[i] > X:
        print(i)
        break