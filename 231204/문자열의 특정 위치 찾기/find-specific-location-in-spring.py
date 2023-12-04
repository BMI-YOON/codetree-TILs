arr = input().split()
string = arr[0]
char = arr[1]
if char in string:
    print(string.index(char))
else:
    print('No')