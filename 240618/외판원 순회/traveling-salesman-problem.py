import sys

n = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]
answer = sys.maxsize
arr = [0]
visited = [False] * n
visited[0] = True

def f(i):
    global answer 

    if i == n:
        sum_val = 0
        for idx in range(1, n):
            sum_val += grid[arr[idx-1]][arr[idx]]
        sum_val += grid[arr[-1]][0]
        answer = min(answer, sum_val)
        return
    
    for num in range(n):
        if visited[num] == True or grid[arr[-1]][num] == 0:
            continue
        arr.append(num)
        visited[num] = True 
        f(i+1)
        arr.pop()
        visited[num] = False 

f(1)
print(answer)