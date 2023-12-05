n, m, p = tuple(map(int, input().split()))
arr = []
for _ in range(m):
    arr.append(tuple(input().split()))

cnt = [0] * 26
for i in range(p-1, m):
    cnt[ord(arr[i][0]) - ord('A')] = 1
for i in range(p-2, -1, -1):
    if arr[i][1] == arr[p-1][1]:
        cnt[ord(arr[i][0]) - ord('A')] = 1
    else:
        break


if arr[p-1][1] == '0':
    print()
else:
    for i in range(n):
        if cnt[i] == 0:
            print(chr(i + 65), end = ' ')