A_arr = input().split()
A_age, A_sex = int(A_arr[0]), A_arr[1]
B_arr = input().split()
B_age, B_sex = int(B_arr[0]), B_arr[1]

if (A_age >= 19 and A_sex == 'M') or (B_age >= 19 and B_sex == 'M'):
    print(1)
else:
    print(0)