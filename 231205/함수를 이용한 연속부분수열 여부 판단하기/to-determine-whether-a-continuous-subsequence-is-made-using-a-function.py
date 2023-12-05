def f(arr1, arr2):
    if arr1 == arr2:
        return True
    else:
        return False

n1, n2 = tuple(map(int, input().split()))
arr1 = input().split()
arr2 = input().split()
boolean = False
for i in range(n1 - n2 + 1):
    if f(arr1[i:n2+i], arr2):
        boolean = True
if boolean == False:
    print("No")
else:
    print("Yes")