string1, string2 = tuple(input().split())
arr = list(string2)
arr[:2] = string1[:2]
string2 = ''.join(arr)
print(string2)