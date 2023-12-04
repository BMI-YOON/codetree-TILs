string = input()
for elem in string:
    if elem.isalpha():
        print(elem.lower(), end = '')
    elif elem.isdigit():
        print(elem, end = '')