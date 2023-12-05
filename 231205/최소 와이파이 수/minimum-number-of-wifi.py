n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
wifi = [0] * n
i = 0
while i < n:
    if arr[i] == 1:
        wifi[min(i + m, n-1)] = 1
        i += 2 * m + 1
    else:
        i += 1
print(sum(wifi))