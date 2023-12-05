def f(M, D):
    if M > 12:
        return "No"
    elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D <= 31:
            return "Yes"
        else:
            return "No"
    elif M == 2:
        if D <= 28:
            return "Yes"
        else:
            return "No"
    else:
        if D <= 30:
            return "Yes"
        else:
            return "No"

M, D = tuple(map(int, input().split()))
print(f(M, D))