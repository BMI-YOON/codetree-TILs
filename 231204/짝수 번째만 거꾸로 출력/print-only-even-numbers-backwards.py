string = input()
if len(string) % 2 == 0:
    print(string[::-2])
else:
    print(string[-2::-2])