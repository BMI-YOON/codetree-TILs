n = int(input())
arr = []
for _ in range(n):
    string = input()
    arr.append(string)

arr.sort()
for elem in arr:
    print(elem)