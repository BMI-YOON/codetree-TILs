string = input()
for elem in string:
    if 'A' <= elem <= 'Z':
        print(elem.lower(), end = '')
    else:
        print(elem.upper(), end = '')