a, b = tuple(map(int, input().split()))
print(a, end = ' ')
for _ in range(9):
    print(b, end = ' ')
    a, b = b, 2 * a + b