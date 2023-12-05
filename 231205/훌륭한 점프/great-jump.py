n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
def f(num):
    new_arr = [idx for idx, elem in enumerate(arr) if elem <= num]
    for i in range(1, len(new_arr)):
        dist = new_arr[i] - new_arr[i-1]
        if dist > k:
            return False
    return True

ans = 100
for num in range(100, max(arr[0], arr[-1]) - 1, -1):
    if f(num):
        ans = min(ans, num)
print(ans)