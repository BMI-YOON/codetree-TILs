string, q = input().split()
q = int(q)
for _ in range(q):
    num = int(input())
    if num == 1:
        string = string[1:] + string[0]
        print(string)
    elif num == 2:
        string = string[-1] + string[:-1]
        print(string)
    else:
        string = string[::-1]
        print(string)