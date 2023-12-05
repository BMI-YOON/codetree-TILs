n = int(input())
honor = 'ABC'
A, B, C, cnt = 0, 0, 0, 0
for _ in range(n):
    char, num = input().split()
    if char == 'A':
        A += int(num)
    if char == 'B':
        B += int(num)
    if char == 'C':
        C += int(num)
    
    if A > B and A > C:
        if honor != 'A':
            cnt += 1
            honor = 'A'
    if B > A and B > C:
        if honor != 'B':
            cnt += 1
            honor = 'B'
    if C > A and C > B:
        if honor !='C':
            cnt += 1
            honor = 'C'
    if A == B and A > C:
        if honor != 'AB':
            cnt += 1
            honor = 'AB'
    if B == C and B > A:
        if honor != 'BC':
            cnt += 1
            honor = 'BC'
    if C == A and A > B:
        if honor != 'CA':
            cnt += 1
            honor = 'CA'
    if A == B and B == C:
        if honor != 'ABC':
            cnt += 1
            honor = 'ABC'

print(cnt)