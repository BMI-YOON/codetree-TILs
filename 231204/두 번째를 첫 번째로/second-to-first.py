string = input()
arr = list(string)
for i in range(len(arr)):
    if arr[i] == string[1]:
        arr[i] = string[0]
string = ''.join(arr)
print(string)