def f(string):
    if string == string[::-1]:
        return True
    else:
        return False

A = input()
if f(A):
    print("Yes")
else:
    print("No")