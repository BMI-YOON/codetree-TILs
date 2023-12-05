binary = list(input())
num = 0
for i in range(len(binary)):
    num = 2 * num + int(binary[i])
print(num)