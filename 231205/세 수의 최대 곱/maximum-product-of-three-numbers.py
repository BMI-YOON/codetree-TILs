import sys
n = int(input())
arr = list(map(int, input().split()))

ans = -sys.maxsize
arr1 = []
arr2 = []

for i in range(n):
    if arr[i] == 0:
        ans = 0
    if arr[i] > 0:
        arr1.append(arr[i])
    if arr[i] < 0:
        arr2.append(arr[i])

arr1.sort(reverse = True)
arr2.sort(reverse = True)

if len(arr1) >= 3:
    ans = max(ans, arr1[0] * arr1[1] * arr1[2])
if len(arr2) >= 3:
    ans = max(ans, arr2[0] * arr2[1] * arr2[2])
if len(arr1) >= 2 and len(arr2) >= 1:
    ans = max(ans, arr1[-1] * arr1[-2] * arr2[0])
if len(arr2) >= 2 and len(arr1) >= 1:
    ans = max(ans, arr1[0] * arr2[-1] * arr2[-2])

print(ans)