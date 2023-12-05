arr = list(input())
cnt = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == '(' and arr[j] == ')':
            cnt += 1
print(cnt)