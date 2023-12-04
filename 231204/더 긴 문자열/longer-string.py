string = input().split()
string1 = string[0]
string2 = string[1]
if len(string1) > len(string2):
    print(string1, len(string1))
elif len(string1) == len(string2):
    print("same")
else:
    print(string2, len(string2))