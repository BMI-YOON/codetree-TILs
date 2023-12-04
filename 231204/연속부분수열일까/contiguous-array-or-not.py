n1, n2 = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
cnt = -1
for i in range(0, n1 - n2 + 1):
    for j in range(0, n2):
        if arr1[i + j] != arr2[j]:
            break
        if j == n2 -1:
            cnt = 0
if cnt == 0:
    print("Yes")
else:
    print("No")