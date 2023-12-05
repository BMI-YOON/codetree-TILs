def f1(N):
    if N == 0:
        return
    f1(N-1)
    print(N, end = ' ')

def f2(N):
    if N == 0:
        return 
    print(N, end = ' ')
    f2(N-1)

N = int(input())
f1(N)
print()
f2(N)