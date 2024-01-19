K, N = map(int, input().split())

arr = []
def print_arr():
    for elem in arr:
        print(elem, end = ' ')
    print()
    return 

def f(n):
    if n == N+1:
        print_arr()
        return
    for i in range(K):
        arr.append(i+1)
        f(n+1)
        arr.pop()

f(1)