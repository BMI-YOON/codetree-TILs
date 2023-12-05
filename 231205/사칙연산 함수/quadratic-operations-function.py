def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a // b

def multiplication(a, b):
    return a * b

a, o, b = input().split()
a = int(a)
b = int(b)

if o == '+':
    print(f"{a} {o} {b} = {addition(a, b)}")
elif o == '-':
    print(f"{a} {o} {b} = {subtraction(a, b)}")
elif o == '*':
    print(f"{a} {o} {b} = {multiplication(a, b)}")
elif o == '/':
    print(f"{a} {o} {b} = {division(a, b)}")
else:
    print("False")