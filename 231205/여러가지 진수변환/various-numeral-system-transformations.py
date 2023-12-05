N, B = tuple(map(int, input().split()))
digits = []
while True:
    if N < B:
        digits.append(N)
        break
    digits.append(N % B)
    N //= B 
for elem in digits[::-1]:
    print(elem, end = '')