N = int(input())
arr = list(map(int, input().split()))
cnt1, cnt2 = 0, 0
for elem in arr:
    if elem % 2 == 0:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 > cnt2:
    print(cnt2 * 2 + 1)
if cnt1 == cnt2:
    print(cnt2 * 2)
if cnt1 < cnt2:
    if (cnt2 - cnt1) % 3 == 0:
        print(cnt1 * 2 + (cnt2 - cnt1) // 3 * 2)
    elif (cnt2 - cnt1) % 3 == 1:
        print(cnt1 * 2 + (cnt2 - cnt1) // 3 * 2 - 1)
    else:
        print(cnt1 * 2 + (cnt2 - cnt1) // 3 * 2 + 1)