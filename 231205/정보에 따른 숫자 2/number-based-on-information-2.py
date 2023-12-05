import sys

T, a, b = tuple(map(int, input().split()))
arr = [0] * 1001
for _ in range(T):
    char, num = input().split()
    arr[int(num)] = char 

def S(x):
    min_val = sys.maxsize
    for i in range(1001):
        if arr[i] == 'S':
            min_val = min(min_val, abs(x - i))
    return min_val

def N(x):
    min_val = sys.maxsize 
    for i in range(1001):
        if arr[i] == 'N':
            min_val = min(min_val, abs(x - i))
    return min_val

cnt = 0
for x in range(a, b+1):
    if S(x) <= N(x):
        cnt += 1
print(cnt)