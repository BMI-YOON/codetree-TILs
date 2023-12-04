a, b = tuple(map(int, input().split()))
print(a, end = ' ')
for _ in range(9):
    print(b, end = ' ')
    a, b = b, (a + b) % 10