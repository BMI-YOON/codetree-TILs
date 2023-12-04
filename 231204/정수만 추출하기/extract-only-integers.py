A, B = input().split()
new_A = new_B = ''
for elem in A:
    if elem.isdigit():
        new_A += elem
    else:
        break
for elem in B:
    if elem.isdigit():
        new_B += elem
    else:
        break
print(int(new_A) + int(new_B))