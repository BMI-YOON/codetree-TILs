n = int(input())
selected = list()
cnt = 0

def check():
    global n, selected 

    for i in range(n-1):
        if selected[i] == selected[i+1]:
            return False
    for i in range(n-3):
        if selected[i:i+2] == selected[i+2:i+4]:
            return False
    for i in range(n-5):
        if selected[i:i+3] == selected[i+3:i+6]:
            return False 
    return True

def simulate(cur):
    global n, selected, cnt 

    if cur == n:
        if check():
            if not cnt:
                for elem in selected:
                    print(elem, end = '')
            cnt = 1
        return 
    for num in range(4, 7):
        selected.append(num)
        simulate(cur+1)
        selected.pop()

simulate(0)