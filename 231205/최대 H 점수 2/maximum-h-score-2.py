N, L = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def f(H):
    cnt1, cnt2 = 0, 0
    for i in range(N):
        if arr[i] <= H - 2:
            continue
        elif arr[i] == H - 1:
            cnt1 += 1
        else:
            cnt2 += 1
    return cnt2 + min(cnt1, L)

for i in range(101):
    if f(i) >= i:
        continue 
    else:
        print(i-1)
        break