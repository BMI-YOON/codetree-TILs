n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

for i in range(1, 5001):
    boolean = True
    num = i
    for j in range(n):
        num *= 2
        if arr[j][0] <= num and num <= arr[j][1]:
            continue
        else:
            boolean = False
    if boolean == True:
        print(i)
        break