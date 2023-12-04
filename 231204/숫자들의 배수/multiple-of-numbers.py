n = int(input())
cnt = 0
num = n
arr = []
while True:
    if cnt == 2:
        break
    arr.append(num)
    if num % 5 == 0:
        cnt += 1
    num += n 
for elem in arr:
    print(elem, end = ' ')