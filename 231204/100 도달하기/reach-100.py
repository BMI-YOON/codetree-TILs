n = int(input())
a, b = 1, n
print(1, end = ' ')
while True:
    print(b, end = ' ')
    if b > 100:
        break
    a, b = b, a + b