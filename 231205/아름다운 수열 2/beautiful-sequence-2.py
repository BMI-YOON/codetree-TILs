N, M = tuple(map(int, input().split()))
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
arr_B.sort()
cnt = 0
for i in range(N - M + 1):
    new_arr = sorted(arr_A[i: i+M])
    if new_arr == arr_B:
        cnt += 1
print(cnt)