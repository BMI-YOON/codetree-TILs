n = int(input())
arr = input().split()
cnt = 0
for i in range(n):
    if arr[i] != chr(65 + i):
        target = -1
        for j in range(i+1, n):
            if arr[j] == chr(65 + i):
                target = j
                break
        for j in range(target, i, -1):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            cnt += 1
print(cnt)