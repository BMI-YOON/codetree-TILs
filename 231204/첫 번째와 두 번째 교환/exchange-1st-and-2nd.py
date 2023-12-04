string = input()
char1 = string[0]
char2 = string[1]
arr = list(string)
for i in range(len(arr)):
    if arr[i] == char1:
        arr[i] = char2 
    elif arr[i] == char2:
        arr[i] = char1 
string = ''.join(arr)
print(string)