n = int(input())
total_len = 0
cnt = 0
for _ in range(n):
    string = input()
    total_len += len(string)
    if string[0] == 'a':
        cnt += 1
print(total_len, cnt)