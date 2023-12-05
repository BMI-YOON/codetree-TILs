n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cnt = [0] * 101
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                for m in range(arr[l][0], arr[l][1]+1):
                    cnt[m] += 1
            boolean = True
            for elem in cnt:
                if elem >= 2:
                    boolean = False
            if boolean:
                ans += 1
print(ans)