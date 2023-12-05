def f(arr):
    count_arr = [0] * 26
    for elem in arr:
        count_arr[ord(elem) - ord('a')] += 1
    cnt = 0
    for elem in count_arr:
        if elem > 0:
            cnt += 1
    if cnt > 1:
        return True
    else:
        return False

A = input()
if f(A):
    print("Yes")
else:
    print("No")