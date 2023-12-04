while True:
    num = int(input())
    if num < 25:
        print("Higher")
    if num > 25:
        print("Lower")
    if num == 25:
        print("Good")
        break