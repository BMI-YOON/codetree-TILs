A, B, X, Y = tuple(map(int, input().split()))
case1 = abs(B-A)
case2 = abs(X-A) + abs(B-Y)
case3 = abs(Y-A) + abs(B-X)
min_val = min(case1, case2)
min_val = min(min_val, case3)
print(min_val)