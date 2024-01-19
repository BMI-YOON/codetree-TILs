n = int(input())
cnt = 0
arr = []

def f(len):
    global cnt
    if len > n:
        return
    if len == n:
        cnt += 1
    for cur in range(1, 5):
        for _ in range(cur):
            arr.append(cur)
        f(len+cur)
        for _ in range(cur):
            arr.pop()
    
f(1)
print(cnt)