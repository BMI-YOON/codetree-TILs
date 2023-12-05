N, M = tuple(map(int, input().split()))
arr_A = [0] * 1000001
arr_B = [0] * 1000001
time = 0
for _ in range(N):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        arr_A[time + 1] = arr_A[time] + v
        time += 1
time = 0
for _ in range(M):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        arr_B[time + 1] = arr_B[time] + v
        time += 1
cnt = 0
cur = 'AB'
for i in range(1, time + 1):
    if cur == 'AB':
        if arr_A[i] > arr_B[i]:
            cur = 'A'
        elif arr_A[i-1] < arr_B[i-1]:
            cur = 'B'
    elif arr_A[i] > arr_B[i] and arr_A[i-1] < arr_B[i-1]:
        cnt += 1
        cur = 'A'
    elif arr_A[i] > arr_B[i] and arr_A[i-1] == arr_B[i-1]:
        if cur =='B':
            cnt += 1
        cur = 'A'
    elif arr_A[i] < arr_B[i] and arr_A[i-1] > arr_B[i-1]:
        cnt += 1
        cur = 'B'
    elif arr_A[i] < arr_B[i] and arr_A[i-1] == arr_B[i-1]:
        if cur == 'A':
            cnt += 1
        cur = 'B'
print(cnt)