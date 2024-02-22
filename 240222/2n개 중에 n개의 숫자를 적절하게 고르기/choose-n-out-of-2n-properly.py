import sys 

n = int(input())
arr = list(map(int, input().split()))
sum = sum(arr)

ans = sys.maxsize

def simulate(cur, cnt, sum_selection):
    global n, arr, sum, ans 

    if cnt == n:
        ans = min(ans, abs(sum - 2 * sum_selection))
        return
    
    if cur == 2*n:
        return 
    
    simulate(cur+1, cnt, sum_selection)

    simulate(cur+1, cnt+1, sum_selection+arr[cur])

simulate(0, 0, 0)
print(ans)