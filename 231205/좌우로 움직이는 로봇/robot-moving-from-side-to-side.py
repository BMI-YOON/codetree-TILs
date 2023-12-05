n, m = tuple(map(int, input().split()))
arr_A = [0] * 1000001
arr_B = [0] * 1000001

time = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'R':
            arr_A[time+1] = arr_A[time] + 1
            time += 1
        else:
            arr_A[time+1] = arr_A[time] - 1
            time += 1
while time < 1000000:
    arr_A[time + 1] = arr_A[time]
    time += 1

time = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'R':
            arr_B[time+1] = arr_B[time] + 1
            time += 1
        else:
            arr_B[time+1] = arr_B[time] - 1
            time += 1
while time < 1000000:
    arr_B[time + 1] = arr_B[time]
    time += 1

cnt = 0
for i in range(1, 1000001):
    if arr_A[i] == arr_B[i] and arr_A[i-1] != arr_B[i-1]:
        cnt += 1
print(cnt)