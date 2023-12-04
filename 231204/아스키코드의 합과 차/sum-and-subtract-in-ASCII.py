a, b = input().split()
if ord(a) >= ord(b):
    print(ord(a) + ord(b), ord(a) - ord(b))
else:
    print(ord(a) + ord(b), ord(b) - ord(a))