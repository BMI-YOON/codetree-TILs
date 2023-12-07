n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            gold = 0
            for ii in range(n):
                for jj in range(n):
                    if abs(ii - i) + abs(jj - j) <= k:
                        gold += arr[ii][jj]
            if gold * m >= k*k + (k+1)*(k+1):
                max_val = max(max_val, gold)
print(max_val)