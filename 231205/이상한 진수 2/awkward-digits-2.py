a = list(map(int, list(input())))

def cal():
    cur = a[0]
    for i in range(1, len(a)):
        cur = cur * 2 + a[i]
    return cur 


max_num = 0
for i in range(len(a)):
    a[i] = 1 - a[i]
    max_num = max(max_num, cal())
    a[i] = 1 - a[i]
print(max_num)