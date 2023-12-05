n = int(input())
honor = 'AB'
A, B, cnt = 0, 0, 0
for _ in range(n):
    char, num = input().split()
    if char == 'A':
        A += int(num)
    else:
        B += int(num)
    if A > B:
        if honor != 'A':
            cnt += 1
            honor = 'A'
    elif A == B:
        if honor != 'AB':
            cnt += 1
            honor = 'AB'
    else:
        if honor != 'B':
            cnt += 1
            honor = 'B'
print(cnt)