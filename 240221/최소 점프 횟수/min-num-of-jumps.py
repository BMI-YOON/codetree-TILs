import sys

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize

def simulate(cur, cnt):
    global n, arr, ans 

    if cur == n-1:
        ans = min(ans, cnt)
        return
    for next in range(cur+1, cur+arr[cur]+1):
        simulate(next, cnt+1)

simulate(0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)