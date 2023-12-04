A = input()
B = input()
new_A = new_B = ''
for elem in A:
    if elem.isdigit():
        new_A += elem 
for elem in B:
    if elem.isdigit():
        new_B += elem 
print(int(new_A) + int(new_B))