n = int(input())
string = input().split()
new_string = ''
for elem in string:
    new_string += elem

for i in range(len(new_string)):
    if i % 5 == 4:
        print(new_string[i])
    else:
        print(new_string[i], end ='')