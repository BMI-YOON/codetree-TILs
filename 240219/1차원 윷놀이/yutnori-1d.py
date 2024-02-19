n, m, k = map(int, input().split())
dist = list(map(int, input().split()))

selected = list()
ans = 0

def simulate(cur):
    global n, m, k, dist, selected, ans

    if cur == n:
        position = [0] * k
        for i, elem in enumerate(selected):
            position[elem-1] += dist[i]
        cnt = 0
        for idx in range(k):
            if position[idx] >= m:
                cnt += 1
        ans = max(ans, cnt)
        return 
    
    for num in range(1, k+1):
        selected.append(num)
        simulate(cur+1)
        selected.pop()

simulate(0)
print(ans)