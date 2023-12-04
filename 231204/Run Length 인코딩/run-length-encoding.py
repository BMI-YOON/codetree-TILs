string = input()
string += 'A'
new = string[0]
cnt = 1
new_string = ''
for i in range(1, len(string)):
    if string[i] == string[i-1]:
        cnt += 1
    else:
        new_string = new_string + string[i-1] + str(cnt)
        new = string[i]
        cnt = 1
print(len(new_string))
print(new_string)