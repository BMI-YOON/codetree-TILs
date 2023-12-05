n, k, T = input().split()
n = int(n)
k = int(k)
arr = []
for _ in range(n):
    string = input()
    if string.find(T) == 0:
        arr.append(string)

arr.sort()
print(arr[k - 1])