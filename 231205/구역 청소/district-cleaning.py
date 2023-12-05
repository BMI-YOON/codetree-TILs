a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

if b < c:
    print((b - a) + (d - c))
elif d < a:
    print((b - a) + (d - c))
elif a <= c and c <= b and b <= d:
    print((b - a) + (d - c) - (b - c))
elif c <= a and a <= d and d <= b:
    print((b - a) + (d - c) - (d - a))
elif a <= c and c <= d and d <= b:
    print((b - a))
else:
    print((d - c))