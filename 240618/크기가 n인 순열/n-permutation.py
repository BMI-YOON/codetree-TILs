n = int(input())
answer = list()
visited = [0] * (n+1)

def choose(i):
    if i == n:
        for elem in answer:
            print(elem, end = ' ')
        print()
        return
    
    for num in range(1, n+1):
        if visited[num] == 1:
            continue

        answer.append(num)
        visited[num] = 1

        choose(i+1)

        answer.pop()
        visited[num] = 0

choose(0)