N = int(input())
arr = list(input())

for length in range(1, N + 1):
    boolean = True 
    for start_idx in range(0, N - length + 1):
        for i in range(0, N - length + 1):
            if i == start_idx:
                continue
            if arr[start_idx:start_idx+length] == arr[i:i+length]:
                boolean = False
    if boolean:
        print(length)
        break