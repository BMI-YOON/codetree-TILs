arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
satisfied = True
for i in range(a, b+1):
    if i % c == 0:
        satisfied = False
if satisfied == True:
    print("YES")
else:
    print("NO")