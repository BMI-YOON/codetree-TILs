n = int(input())
arr = list(map(int, input().split()))
arr.sort()
reversed_arr = list(reversed(arr))
for elem in arr:
    print(elem, end = ' ')
print()
for elem in reversed_arr:
    print(elem, end = ' ')