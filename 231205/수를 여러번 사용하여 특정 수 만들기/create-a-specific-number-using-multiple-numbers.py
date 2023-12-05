A, B, C = tuple(map(int, input().split()))
ans = 0
for a in range(C // A + 1):
    ans = max(ans, a * A + (C - a * A) // B * B)
print(ans)