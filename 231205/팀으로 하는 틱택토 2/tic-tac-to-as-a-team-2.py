def win(i, j, a, b, c):
    if a == i and b == i and c == j:
        return True
    if a == i and b == j and c == i:
        return True
    if a == j and b == i and c == i:
        return True 
    if a == j and b == j and c == i:
        return True 
    if a == j and b == i and c == j:
        return True 
    if a == i and b == j and c == j:
        return True
    return False 

arr = [
    list(map(int, list(input())))
    for _ in range(3)
]

cnt = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        boolean = False 
        if win(i, j, arr[0][0], arr[0][1], arr[0][2]):
            boolean = True
        if win(i, j, arr[1][0], arr[1][1], arr[1][2]):
            boolean = True 
        if win(i, j, arr[2][0], arr[2][1], arr[2][2]):
            boolean = True 
        if win(i, j, arr[0][0], arr[1][0], arr[2][0]):
            boolean = True 
        if win(i, j, arr[0][1], arr[1][1], arr[2][1]):
            boolean = True 
        if win(i, j, arr[0][2], arr[1][2], arr[2][2]):
            boolean = True 
        if win(i, j, arr[0][0], arr[1][1], arr[2][2]):
            boolean = True 
        if win(i, j, arr[2][0], arr[1][1], arr[0][2]):
            boolean = True 
        if boolean:
            cnt += 1
print(cnt)