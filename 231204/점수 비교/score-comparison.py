A_arr = input().split()
A_math, A_english = int(A_arr[0]), int(A_arr[1])
B_arr = input().split()
B_math, B_english = int(B_arr[0]), int(B_arr[1])
if A_math > B_math and A_english > B_english:
    print(1)
else: 
    print(0)