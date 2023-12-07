n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))

def f():
    global arr
    tmp_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            tmp_arr.append(arr[i])
    arr = tmp_arr.copy()

for i in range(s1-1, e1):
    arr[i] = 0
f()

for i in range(s2-1, e2):
    arr[i] = 0
f()

print(len(arr))
for elem in arr:
    print(elem)