string = input()
order = input()
for elem in order:
    if elem == 'L':
        string = string[1:] + string[0]
    else:
        string = string[-1] + string[:-1]
print(string)