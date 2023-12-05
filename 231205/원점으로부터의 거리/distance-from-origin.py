class Dot:
    def __init__(self, n, d):
        self.n = n
        self.d = d 

N = int(input())
dots = []
for i in range(1, N + 1):
    x, y = tuple(map(int, input().split()))
    dots.append(Dot(i, (x if x >= 0 else -x) + (y if y >= 0 else -y)))
dots.sort(key = lambda x: (x.d, x.n))
for dot in dots:
    print(dot.n)