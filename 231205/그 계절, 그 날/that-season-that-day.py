def f1(Y):
    if Y % 400 == 0:
        return True
    if Y % 100 == 0:
        return False
    if Y % 4 == 0:
        return True 
    return False 

def f2(Y, M, D):
    if f1(Y):
        if M == 2:
            if D <= 29:
                return "Winter"
            else:
                return -1
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if D > 31:
                return -1
            else:
                if M == 3 or M == 5:
                    return "Spring"
                if M ==7 or M == 8:
                    return "Summer"
                if M == 10:
                    return "Fall"
                if M == 12 or M == 1:
                    return "Winter"
        else:
            if D > 30:
                return -1
            else:
                if M == 4:
                    return "Spring"
                if M == 6:
                    return "Summer"
                if M == 9 or M == 11:
                    return "Fall"

    else:
        if M == 2:
            if D <= 28:
                return "Winter"
            else:
                return -1
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if D > 31:
                return -1
            else:
                if M == 3 or M == 5:
                    return "Spring"
                if M ==7 or M == 8:
                    return "Summer"
                if M == 10:
                    return "Fall"
                if M == 12 or M == 1:
                    return "Winter"
        else:
            if D > 30:
                return -1
            else:
                if M == 4:
                    return "Spring"
                if M == 6:
                    return "Summer"
                if M == 9 or M == 11:
                    return "Fall"

Y, M, D = tuple(map(int, input().split()))
print(f2(Y, M, D))