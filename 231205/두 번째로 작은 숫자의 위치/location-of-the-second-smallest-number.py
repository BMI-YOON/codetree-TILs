n = int(input())
arr = list(map(int, input().split()))
min_val = min(arr)
second_min = 101
for i in range(n):
    if arr[i] != min_val and arr[i] < second_min:
        second_min = arr[i]
cnt, idx = 0, -1
for i in range(n):
    if arr[i] == second_min:
        cnt += 1
        idx = i
if cnt == 1:
    print(idx + 1)
else:
    print(-1)