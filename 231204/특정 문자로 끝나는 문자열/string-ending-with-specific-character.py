arr = [
    input()
    for _ in range(10)
]
char = input()
boolean = False
for string in arr:
    if string[-1] == char:
        print(string)
        boolean = True
if boolean == False:
    print("None")