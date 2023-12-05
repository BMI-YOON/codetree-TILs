class B:
    def __init__(self, num, cnt1, cnt2):
        self.num = num 
        self.cnt1 = cnt1
        self.cnt2 = cnt2 

def get_cnt1(i, j, k, num):
    cnt = 0
    c = num % 10
    num //= 10
    b = num % 10
    num //= 10
    a = num % 10
    if k == c:
        cnt += 1
    if j == b:
        cnt += 1
    if i == a:
        cnt += 1
    return cnt 

def get_cnt2(i, j, k, num):
    cnt = 0
    c = num % 10
    num //= 10
    b = num % 10
    num //= 10
    a = num % 10
    if (i == c or j == c):
        cnt += 1
    if (i == b or k == b):
        cnt += 1
    if (j == a or k == a):
        cnt += 1
    return cnt

N = int(input())
b = []
for _ in range(N):
    num, cnt1, cnt2 = tuple(map(int, input().split()))
    b.append(B(num, cnt1, cnt2))

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            boolean = True
            for l in range(N):
                if get_cnt1(i, j, k, b[l].num) != b[l].cnt1 or get_cnt2(i, j, k, b[l].num) != b[l].cnt2:
                    boolean = False
            if boolean == True:
                cnt += 1
print(cnt)