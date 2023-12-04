string = input()
L = len(string)
for _ in range(L+1):
    print(string)
    string = string[-1] + string[:-1]