n, m = map(int, input().split())
arr = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

selected = list()
minimum = m 

def go(num):
    global selected
    cur = 15
    while cur > 0:
        if (num, cur) in selected:
            num += 1
        elif (num-1, cur) in selected:
            num -= 1
        cur -= 1
    return num 

def cal():
    global n, selected 
    candidate = list()
    for i in range(1, n+1):
        candidate.append(go(i))
    return candidate 

for i in range(m):
    selected.append(arr[i])
ans = cal()
for i in range(m):
    selected.pop()

def simulate(k):
    global n, m, arr, selected, minimum, ans
    if k == m:
        candidate = cal()
        if candidate == ans:
            minimum = min(m, len(candidate))
        return 
    simulate(k+1)
    selected.append((arr[k][0], arr[k][1]))
    simulate(k+1)
    selected.pop()

simulate(0)
print(minimum)