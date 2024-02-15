n = int(input())
arr = list()
for _ in range(n):
    x1, x2 = map(int, input().split())
    arr.append((x1, x2))

selected = list()
ans = 0

def f(x1, x2, selected):
    for i in range(len(selected)):
        if selected[i][0] <= x1 <= selected[i][1]:
            return False
        if selected[i][0] <= x2 <= selected[i][1]:
            return False
    return True

def simulate(num):
    global n, arr, selected, ans 

    if num == n:
        return 
    simulate(num+1)
    x1, x2 = arr[num][0], arr[num][1]
    if f(x1, x2, selected):
        selected.append((arr[num][0], arr[num][1]))
        ans = max(ans, num+1)
        simulate(num+1)

simulate(0)
print(ans)