n = int(input())
arr = [
    input()
    for _ in range(n)
]
char = input()
cnt = total_len = 0
for string in arr:
    if string[0] == char:
        cnt += 1
        total_len += len(string)
print(cnt, f"{total_len / cnt:.2f}")