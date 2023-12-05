class Handshake:
    def __init__(self, t, x, y):
        self.t = t 
        self.x = x 
        self.y = y

handshakes = []
N, K, P, T = tuple(map(int, input().split()))
for _ in range(T):
    t, x, y = tuple(map(int, input().split()))
    handshakes.append(Handshake(t, x, y))
handshakes.sort(key = lambda x: x.t)
ans = [0] * (N+1)
cnt = [0] * (N+1)
ans[P] = 1
for handshake in handshakes:
    if ans[handshake.x] == 1 and ans[handshake.y] == 1:
        cnt[handshake.x] += 1
        cnt[handshake.y] += 1
    elif ans[handshake.x] == 1 and ans[handshake.y] != 1:
        if cnt[handshake.x] < K:
            ans[handshake.y] = 1
            cnt[handshake.x] += 1
    elif ans[handshake.x] != 1 and ans[handshake.y] == 1:
        if cnt[handshake.y] < K:
            ans[handshake.x] = 1
            cnt[handshake.y] += 1
for i in range(1, N+1):
    print(ans[i], end = '')