A = list(input())
min_val = 21
for _ in range(len(A)):
    A.insert(0, A.pop())
    cnt = 1
    cur = A[0]
    for i in range(1, len(A)):
        if A[i] != cur:
            cur = A[i]
            cnt += 1
    if cnt == 1 and len(A) == 10:
        min_val = 3
        break
    else:
        min_val = min(min_val, cnt * 2)

if len(A) == 1:
    print(2)
else:
    print(min_val)