def f(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -arr[i]

N = int(input())
arr = list(map(int, input().split()))
f(arr)
for elem in arr:
    print(elem, end = ' ')