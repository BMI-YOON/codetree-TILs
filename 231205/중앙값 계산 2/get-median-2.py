n = int(input())
arr = list(map(int, input().split()))
cur_arr = []
for i in range(n):
    cur_arr.append(arr[i])
    if i % 2 == 0:
        cur_arr.sort()
        print(cur_arr[i//2], end = ' ')