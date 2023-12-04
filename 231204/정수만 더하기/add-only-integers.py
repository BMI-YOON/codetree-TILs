string = input()
sum = 0
for elem in string:
    if elem.isdigit():
        sum += int(elem)
print(sum)