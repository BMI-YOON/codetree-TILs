string = input()
while len(string) > 1:
    index = int(input())
    arr = list(string)
    if index < len(string):
        arr.pop(index)
    else:
        arr.pop()
    string = ''.join(arr)
    print(string)