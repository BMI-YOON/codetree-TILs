n = int(input())
cur_arr = ['no'] * 200000 
white_arr = [0] * 200000 
black_arr = [0] * 200000 
cur = 100000
for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(cur, cur - x, -1):
            white_arr[i] += 1
            if white_arr[i] >= 2 and black_arr[i] >= 2:
                cur_arr[i] = 'gray'
            else:
                cur_arr[i] = 'white'
        cur -= (x - 1)
    else:
        for i in range(cur, cur + x, 1):
            black_arr[i] += 1
            if white_arr[i] >= 2 and black_arr[i] >= 2:
                cur_arr[i] = 'gray'
            else:
                cur_arr[i] = 'black'
        cur += (x - 1)

cnt_white = cnt_black = cnt_gray = 0
for elem in cur_arr:
    if elem == 'white':
        cnt_white += 1
    if elem == 'black':
        cnt_black += 1
    if elem == 'gray':
        cnt_gray += 1
print(cnt_white, cnt_black, cnt_gray)