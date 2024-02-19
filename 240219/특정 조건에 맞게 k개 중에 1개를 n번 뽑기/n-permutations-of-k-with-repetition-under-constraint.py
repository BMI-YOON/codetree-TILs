K, N = map(int, input().split())
selected = list()

def simulate(cur):
    global K, N, selected 

    if cur == N:
        for elem in selected:
            print(elem, end = ' ')
        print()
        return
    
    for num in range(1, K+1):
        if len(selected) >= 2 and (selected[-2] == selected[-1] and selected[-1] == num):
            continue
        selected.append(num)
        simulate(cur+1)
        selected.pop()

simulate(0)