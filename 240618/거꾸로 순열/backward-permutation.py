n = int(input())
answer = list()
visited = [False] * (n+1)

def f(i):
    if i == n:
        for elem in answer:
            print(elem, end = ' ')
        print()
    
    for num in range(n, 0, -1):
        if visited[num] == True:
            continue
        
        answer.append(num)
        visited[num] = True 

        f(i+1)

        answer.pop()
        visited[num] = False 

f(0)