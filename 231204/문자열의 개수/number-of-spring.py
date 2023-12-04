cnt = 0
arr = []
while True:
    string = input()
    if string == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        arr.append(string)
print(cnt)
for elem in arr:
    print(elem)