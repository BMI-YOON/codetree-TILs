import copy

class Gift:
    def __init__(self, p, s):
        self.p = p
        self.s = s 

N, B = tuple(map(int, input().split()))
gifts = []
for _ in range(N):
    p, s = tuple(map(int, input().split()))
    gifts.append(Gift(p, s))

ans = 0
for i in range(N):
    new_gifts = copy.deepcopy(gifts)
    p, s = new_gifts[i].p, new_gifts[i].s 
    new_gifts[i].p, new_gifts[i].s = -1, -1 
    new_gifts.sort(key = lambda x: x.p + x.s)
    new_gifts[0].p, new_gifts[0].s = p // 2, s 

    sum = 0
    for j in range(N):
        sum += new_gifts[j].p + new_gifts[j].s 
        if sum <= B:
            ans = max(ans, j + 1)
print(ans)