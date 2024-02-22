N, M = map(int, input().split())

selected = list()

def simulate(cur, cnt):
    if cnt == M:
        for elem in selected:
            print(elem, end = ' ')
        print()
    
    for next in range(cur+1, N+1):
        selected.append(next)
        simulate(next, cnt+1)
        selected.pop()

simulate(0, 0)