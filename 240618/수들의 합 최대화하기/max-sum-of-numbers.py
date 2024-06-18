n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]
answer = -1
arr = list()
visited = [False] * (n+1)

def f(i):
    global answer 
    
    if i == n:
        candidate = 0
        for row in range(n):
            candidate += grid[row][arr[row]-1]
        answer = max(answer, candidate)
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