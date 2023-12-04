A = input().split()
Am, Ae = int(A[0]), int(A[1])
B = input().split()
Bm, Be = int(B[0]), int(B[1])
if Am > Bm:
    print("A")
elif Am < Bm:
    print("B")
elif Ae > Be:
    print("A")
else:
    print("B")