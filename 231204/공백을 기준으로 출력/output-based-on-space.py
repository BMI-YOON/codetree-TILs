string1 = input()
string2 = input()
string = string1+string2
for i in range(len(string)):
    if string[i] != ' ':
        print(string[i], end = '')