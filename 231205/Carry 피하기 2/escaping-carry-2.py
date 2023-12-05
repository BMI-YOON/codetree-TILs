def carry(a, b, c):
    while not (a == 0 and b == 0 and c == 0):
        if a % 10 + b % 10 + c % 10 >= 10:
            return True
        a, b, c = a // 10, b // 10, c // 10
    return False

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

max_num = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not carry(arr[i], arr[j], arr[k]):
                max_num = max(max_num, arr[i] + arr[j] + arr[k])
print(max_num)