n = int(input())
selected = list()
cnt = 0

def check():
    global n, selected 
    max_length = int(n/2)
    for length in range(1, max_length + 1):
        for i in range(n-length*2+1):
            if selected[i:i+length] == selected[i+length:i+length+length]:
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