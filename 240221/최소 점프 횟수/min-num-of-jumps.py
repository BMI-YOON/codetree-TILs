import sys

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize

def simulate(cur, cnt):
    global n, arr, ans 

    if cur == n-1:
        ans = min(ans, cnt)
        return
    if arr[cur] == 0:
        return 
    else:
        for next in range(cur+1, min(cur+arr[cur]+1, n)):
            simulate(next, cnt+1)

simulate(0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)