arr_2d = [
    input().split()
    for _ in range(5)
]
for i in range(5):
    for j in range(3):
        print(chr(ord(arr_2d[i][j]) - 32), end = ' ')
    print()