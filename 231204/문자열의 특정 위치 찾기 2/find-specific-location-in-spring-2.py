arr = ["apple", "banana", "grape", "blueberry", "orange"]
char = input()
cnt = 0
for elem in arr:
    if elem[2] == char or elem[3] == char:
        print(elem)
        cnt += 1
print(cnt)