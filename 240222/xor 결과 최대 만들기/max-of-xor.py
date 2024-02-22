n, m = map(int, input().split())
arr = list(map(int, input().split()))

selected = list()
ans = 0

def cal():
    global selected 
    
    if len(selected) == 0:
        return 0

    output = selected[0]
    for i in range(1, len(selected)):
        output = output ^ selected[i]
    return output

def simulate(cur, cnt):
    global n, m, arr, selected, ans 

    if cur == n:
        if cnt == m:
            ans = max(ans, cal())
        return 

    simulate(cur+1, cnt)

    selected.append(arr[cur])
    simulate(cur+1, cnt+1)
    selected.pop()

simulate(0, 0)
print(ans)