A = input()
B = input()
arr_A = list(A)
arr_B = list(B)
if sorted(arr_A) == sorted(arr_B):
    print("Yes")
else:
    print("No")