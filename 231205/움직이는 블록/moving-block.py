N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

num = sum(arr)
sum = 0
for i in range(N):
    sum += abs(arr[i] - num // N)
print(sum // 2)