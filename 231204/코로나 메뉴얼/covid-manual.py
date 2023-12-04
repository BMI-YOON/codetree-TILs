arr = input().split()
sx1 = arr[0]; bt1 = int(arr[1])
arr = input().split()
sx2 = arr[0]; bt2 = int(arr[1])
arr = input().split()
sx3 = arr[0]; bt3 = int(arr[1])
num = 0
if sx1 == 'Y' and bt1 >= 37:
    num += 1
if sx2 == 'Y' and bt2 >= 37:
    num += 1
if sx3 == 'Y' and bt3 >= 37:
    num += 1
if num >= 2:
    print('E')
else:
    print('N')