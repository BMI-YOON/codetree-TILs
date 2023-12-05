a, b, c = tuple(map(int, input().split()))
if (a - 11) * 24 * 60 + (b - 11) * 60 + (c - 11) < 0:
    print(-1)
else:
    print((a - 11) * 24 * 60 + (b - 11) * 60 + (c - 11))