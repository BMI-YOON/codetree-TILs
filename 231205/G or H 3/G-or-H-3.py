N, K = tuple(map(int, input().split()))
arr = [0] * (10001)
for _ in range(N):
    num, char = input().split()
    num = int(num)
    if char == 'G':
        arr[num] = 1
    if char == 'H':
        arr[num] = 2

max_val = 0
for i in range(1, 10001-K):
    sum = 0
    for j in range(i, i+K+1):
        sum += arr[j]
    max_val = max(max_val, sum)
print(max_val)