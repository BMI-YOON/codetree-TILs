n = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]
answer = -1
arr = list()
visited = [False] * (n+1)

def f(i):
    global answer 

    val = 10001
    if i == n:
        for row in range(n):
            val = min(val, grid[row][arr[row]-1])
        answer = max(answer, val)
        return
    
    for num in range(1, n+1):
        if visited[num] == True:
            continue
        arr.append(num)
        visited[num] = True
        f(i+1)
        arr.pop()
        visited[num] = False 

f(0)
print(answer)