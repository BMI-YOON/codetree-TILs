def swap(n, m):
    n, m = m, n
    return n, m

n, m = tuple(map(int, input().split()))
n, m = swap(n, m)
print(n, m)